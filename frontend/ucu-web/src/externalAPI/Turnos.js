const API_URL = "http://localhost:3006/api/turnos";

const addAuthToRequestBody = (body) => {
  return {
    ...body,
    correo: "admin@mail.com",
    contrasena: "123",
  };
};

export const getAllTurnos = async () => {
  try {
    const response = await fetch(API_URL, {
      method: "GET",
    });
    return await response.json();
  } catch (error) {
    console.error("Error fetching all turnos:", error);
    throw error;
  }
};

export const getTurnoById = async (id) => {
  try {
    const response = await fetch(`${API_URL}/${id}`, {
      method: "GET",
    });
    return await response.json();
  } catch (error) {
    console.error(`Error fetching turno with id ${id}:`, error);
    throw error;
  }
};

export const createTurno = async (turno) => {
  try {
    const requestBody = addAuthToRequestBody(turno);
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });
    return await response.json();
  } catch (error) {
    console.error("Error creating turno:", error);
    throw error;
  }
};

export const updateTurno = async (id, turno) => {
  try {
    const requestBody = addAuthToRequestBody(turno);
    const response = await fetch(`${API_URL}/${id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });
    return await response.json();
  } catch (error) {
    console.error(`Error updating turno with id ${id}:`, error);
    throw error;
  }
};

export const deleteTurno = async (id) => {
  try {
    const requestBody = addAuthToRequestBody({});
    const response = await fetch(`${API_URL}/${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });
    return await response.json();
  } catch (error) {
    console.error(`Error deleting turno with id ${id}:`, error);
    throw error;
  }
};
