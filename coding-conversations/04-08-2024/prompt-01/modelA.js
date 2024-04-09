const jwt = require('jsonwebtoken');

function generateJWT(user) {
    const payload = {
      sub: user.id, // Unique user identifier
      iat: Math.floor(Date.now() / 1000), // Issued at time
      // Optional, but recommended:
      exp: Math.floor(Date.now() / 1000) + (60 * 60) // Expiration (1 hour)
    };
  
    const secret = process.env.JWT_SECRET; // Store this securely!
    return jwt.sign(payload, secret);
  }

  function authenticateToken(req, res, next) {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];
  
    if (!token) return res.sendStatus(401); // Unauthorized
  
    jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
      if (err) return res.sendStatus(403); // Forbidden
      req.user = user;
      next();
    });
  }