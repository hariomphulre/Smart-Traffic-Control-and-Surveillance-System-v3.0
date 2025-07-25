const express = require('express');
const { body } = require('express-validator');
const { register, login, getCurrentUser } = require('./auth.controller');
const authMiddleware = require('./auth.middleware');

const router = express.Router();

router.post('/register', [
  body('name').notEmpty().withMessage('Name is required'),
  body('email').isEmail().withMessage('Valid email is required'),
  body('password').isLength({ min: 6 }).withMessage('Password must be at least 6 characters'),
], register);

router.post('/login', [
  body('email').isEmail().withMessage('Valid email is required'),
  body('password').notEmpty().withMessage('Password is required'),
], login);

router.get('/user', authMiddleware, getCurrentUser);

module.exports = router; 