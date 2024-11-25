const AuthHeader = () => {
  return {
    "Content-Type": "application/json",
    correo: "admin@mail.com",
    contrasena: "123",
  };
};

export const createOptions = (method, body = null) => {
  const options = {
    method: method,
    headers: AuthHeader(),
  };
  if (body) {
    options.body = JSON.stringify(body);
  }
  return options;
};
