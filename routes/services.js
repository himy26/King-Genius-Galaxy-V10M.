const express = require('express');
const router = express.Router();
const jwt = require('jsonwebtoken');

// Middleware to verify token
const auth = (req, res, next) => {
    const token = req.header('x-auth-token');
    if (!token) return res.status(401).json({ msg: 'No token, authorization denied' });

    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET || 'secret');
        req.user = decoded.user;
        next();
    } catch (err) {
        res.status(401).json({ msg: 'Token is not valid' });
    }
};

// Samsung FRP Unlock
router.post('/unlock/samsung-frp', auth, async (req, res) => {
    // Logic for Samsung FRP Unlock would go here
    // For now, we simulate a process
    const { imei } = req.body;

    if (!imei) return res.status(400).json({ msg: 'IMEI is required' });

    // Simulate success
    res.json({
        msg: 'Samsung FRP Unlock request submitted successfully',
        status: 'Processing',
        imei: imei
    });
});

// iCloud Unlock
router.post('/unlock/icloud', auth, async (req, res) => {
    const { imei } = req.body;
    if (!imei) return res.status(400).json({ msg: 'IMEI is required' });

    // Simulate success
    res.json({
        msg: 'iCloud Unlock request submitted successfully',
        status: 'Processing',
        imei: imei
    });
});

module.exports = router;
