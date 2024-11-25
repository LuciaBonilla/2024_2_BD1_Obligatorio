const API_URL_INSTRUCTORES = "http://localhost:3006/api/instructores";
const API_URL_ALUMNOS = "http://localhost:3006/api/alumnos";

const addAuthToRequest = (body) => {
  return {
    ...body,
    correo: "admin@mail.com",
    contrasena: "123",
  };
};


export const getAllAlumnos = async () => {
  try {
    const response = await fetch(API_URL_ALUMNOS, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    return await response.json();
  } catch (error) {
    console.error("Error fetching all alumnos:", error);
    throw error;
  }
};

export const getAlumnoByCI = async (ci) => {
  try {
    const response = await fetch(`${API_URL_ALUMNOS}/${ci}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    return await response.json();
  } catch (error) {
    console.error(`Error fetching alumno with CI ${ci}:`, error);
    throw error;
  }
};

export const createAlumno = async (alumno) => {
  try {
    const requestBody = addAuthToRequest(alumno);
    const response = await fetch(API_URL_ALUMNOS, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });
    return await response.json();
  } catch (error) {
    console.error("Error creating alumno:", error);
    throw error;
  }
};

export const updateAlumno = async (ci, alumno) => {
  try {
    const requestBody = addAuthToRequest(alumno);
    const response = await fetch(`${API_URL_ALUMNOS}/${ci}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });
    return await response.json();
  } catch (error) {
    console.error(`Error updating alumno with CI ${ci}:`, error);
    throw error;
  }
};

export const deleteAlumno = async (ci) => {
  try {
    const requestBody = addAuthToRequest({});
    const response = await fetch(`${API_URL_ALUMNOS}/${ci}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });
    return await response.json();
  } catch (error) {
    console.error(`Error deleting alumno with CI ${ci}:`, error);
    throw error;
  }
};
