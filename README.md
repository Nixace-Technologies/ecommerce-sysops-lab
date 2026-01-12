
# Ecommerce SysOps Lab

Tiny backend service to practice:
- Git
- GitHub workflows
- Branching
- Releases

Run:
python3 app.py


HOW THIS WORKS IN REAL LIFE (IMPORTANT)
Web
fetch("http://server:8000/cart/total", {
  method: "POST",
  body: JSON.stringify(["apple", "milk"])
})

Mobile (Expo / React Native)
Same API call.
CLI (Students)
curl -X POST http://localhost:8000/cart/total \
     -H "Content-Type: application/json" \
     -d '["apple","banana"]'

💡 One backend → many clients
