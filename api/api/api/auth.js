export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.status(200).json({
    project: "LAVENTI INFINITY OS V.12",
    version: "12.0",
    status: "Active",
    tokens: 1500000,
    dedication: "إلى الأستاذة علا مطاوع (أم ملك)",
    owner: "himy26"
  });
}
