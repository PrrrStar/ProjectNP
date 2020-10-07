import React, { useState } from "react";
import { Modal, Button, Form } from "react-bootstrap";

const Login = () => {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
    <>
      <Button variant="primary" onClick={handleShow} className="header__authBtn">
        <img src="/images/person-24px.png" alt="login" />
        <span>Log in</span>
      </Button>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>로그인</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group controlId="">
              <Form.Control autocomplete="off" type="text" placeholder="ID" class="login-modal__input" id="login-user-email" name="email" />
            </Form.Group>
            <Form.Group controlId="">
              <Form.Control autocomplete="off" type="password" placeholder="PASSWORD" class="login-modal__input" id="login-user-password" name="password" />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="primary" href="/" class="login-modal__login" id="btn-login">
            Login
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};

export default Login;
