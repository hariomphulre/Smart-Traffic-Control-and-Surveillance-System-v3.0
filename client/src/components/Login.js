import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import { Form, Button, Card, Alert, Spinner } from 'react-bootstrap';

const Login = () => {
  const { login } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      await login(email, password);
      navigate('/');
    } catch (err) {
      setError(err.response?.data?.message || 'Login failed');
    }
    setLoading(false);
  };

  return (
    <div className="d-flex justify-content-center align-items-center" style={{ minHeight: '100vh', background: 'var(--background-color, #222)' }}>
      <Card style={{ minWidth: 350 }} className="shadow p-4">
        <h2 className="mb-4 text-center">Login</h2>
        {error && <Alert variant="danger">{error}</Alert>}
        <Form onSubmit={handleSubmit}>
          <Form.Group className="mb-3" controlId="loginEmail">
            <Form.Label>Email</Form.Label>
            <Form.Control type="email" value={email} onChange={e => setEmail(e.target.value)} required autoFocus autoComplete="username" />
          </Form.Group>
          <Form.Group className="mb-3" controlId="loginPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" value={password} onChange={e => setPassword(e.target.value)} required autoComplete="current-password" />
          </Form.Group>
          <Button variant="primary" type="submit" className="w-100" disabled={loading}>
            {loading ? <Spinner animation="border" size="sm" /> : 'Login'}
          </Button>
        </Form>
        <div className="mt-3 text-center">
          <span>Don't have an account? <Link to="/signup">Sign up</Link></span>
        </div>
      </Card>
    </div>
  );
};

export default Login; 