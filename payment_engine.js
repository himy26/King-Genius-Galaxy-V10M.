const express = require('express');
const mongoose = require('mongoose');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const paypal = require('@paypal/checkout-server-sdk');
const Razorpay = require('razorpay');
const { v4: uuidv4 } = require('uuid');

const app = express();
app.use(express.json());

// 🔱 سجل المعاملات الملكي (MongoDB Schema)
const TransactionSchema = new mongoose.Schema({
    txid: String,
    amount: Number,
    currency: String,
    gateway: String,
    status: { type: String, default: 'pending' },
    payout_status: { type: String, default: 'none' },
    timestamp: { type: Date, default: Date.now }
});
const Transaction = mongoose.model('Transaction', TransactionSchema);

// 🔱 1. إنشاء عملية الدفع (Create Payment)
app.post('/api/payment/create', async (req, res) => {
    const { amount, currency, gateway } = req.body;
    let payment_data;

    try {
        if (gateway === 'stripe') {
            payment_data = await stripe.paymentIntents.create({
                amount: amount * 100,
                currency: currency,
                payment_method_types: ['card'],
            });
        }
        
        const newTx = await Transaction.create({
            txid: payment_data.id,
            amount, currency, gateway
        });
        
        res.json({ success: true, clientSecret: payment_data.client_secret, txid: newTx.txid });
    } catch (err) { res.status(500).json({ error: err.message }); }
});

// 🔱 2. تأكيد الاستلام والتسييل التلقائي (Webhook Handler)
app.post('/api/payment/webhook', async (req, res) => {
    const event = req.body;
    if (event.type === 'payment_intent.succeeded') {
        const tx = await Transaction.findOneAndUpdate(
            { txid: event.data.object.id },
            { status: 'completed' },
            { new: true }
        );

        // 🔥 نظام الاقتحام البنكي: تسييل فوري إذا تجاوز الحد
        if (tx.amount >= process.env.WITHDRAWAL_THRESHOLD) {
            initiateAutoPayout(tx.amount, tx.currency);
        }
    }
    res.sendStatus(200);
});

// 🔱 3. نظام السحب التلقائي للبنك (Auto-Transfer)
async function initiateAutoPayout(amount, currency) {
    console.log(`🕯️ رادار V10M: جاري تسييل ${amount} ${currency} للملك محمد حسن...`);
    try {
        const payout = await stripe.payouts.create({
            amount: amount * 100,
            currency: currency,
            method: 'instant', // سحب فوري للفيزا المرتبطة
        }, { stripeAccount: process.env.STRIPE_CONNECT_ID });
        
        await Transaction.updateMany({ status: 'completed', payout_status: 'none' }, { payout_status: 'sent_to_bank' });
        console.log("✅ تم ضخ المصاري في الحساب البنكي بنجاح!");
    } catch (err) {
        console.error("⚠️ فشل في نظام السحب: " + err.message);
    }
}

app.listen(process.env.PORT, () => console.log(`🚀 V10M Treasury System Active on Port ${process.env.PORT}`));
