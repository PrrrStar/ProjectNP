import React, { useState } from "react";
import { Modal, Button, Form } from "react-bootstrap";

const SignUp = () => {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
    <>
      <Button variant="primary" onClick={handleShow} className="header__authBtn">
        <img src="/images/person-24px.png" alt="login" />
        <span>Sign up</span>
      </Button>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>회원가입</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group controlId="">
              <Form.Label>이메일</Form.Label>
              <Form.Control type="email" placeholder="메일을 입력해주세요." autoComplete="off" />
            </Form.Group>
            <Form.Group controlId="">
              <Form.Label>닉네임</Form.Label>
              <Form.Control type="text" placeholder="닉네임을 입력해주세요." autoComplete="off" />
            </Form.Group>
            <Form.Group controlId="">
              <Form.Label>비밀번호</Form.Label>
              <Form.Control type="password" placeholder="비밀번호를 입력해주세요." autoComplete="off" />
            </Form.Group>
            <Form.Group controlId="">
              <Form.Label>비밀번호 확인</Form.Label>
              <Form.Control type="password" placeholder="비밀번호를 한번 더 입력해주세요." autoComplete="off" />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Pre
          </Button>
          <Button variant="primary" onClick={handleClose}>
            Complete
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};

export default SignUp;
