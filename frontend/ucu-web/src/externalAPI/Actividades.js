const API_URL = "http://localhost:3006/api/actividades";

const addAuthToRequestBody = (body) => {
  return {
    ...body,
    correo: "admin@mail.com",
    contrasena: "123",
  };
};

export const getAllActividades = async () => {
  try {
    const response = await fetch(API_URL, {
      method: "GET",
    });
    return await response.json();
  } catch (error) {
    console.error("Error fetching all actividades:", error);
    throw error;
  }
};

export const getActividadById = async (id) => {
  try {
    const response = await fetch(`${API_URL}/${id}`, {
      method: "GET",
    });
    return await response.json();
  } catch (error) {
    console.error(`Error fetching actividad with id ${id}:`, error);
    throw error;
  }
};


export const updateActividad = async (id, actividad) => {
  try {
    const requestBody = addAuthToRequestBody(actividad);
    const response = await fetch(`${API_URL}/${id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });
    return await response.json();
  } catch (error) {
    console.error(`Error updating actividad with id ${id}:`, error);
    throw error;
  }
};

export const deleteActividad = async (id) => {
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
    console.error(`Error deleting actividad with id ${id}:`, error);
    throw error;
  }
};