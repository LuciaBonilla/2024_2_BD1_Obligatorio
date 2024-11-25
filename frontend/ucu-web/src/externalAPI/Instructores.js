const API_URL = "http://localhost:3006/api/instructores";

const addAuthToRequestBody = (body) => {
  return {
    ...body,
    correo: "admin@mail.com",
    contrasena: "123",
  };
};

export const getAllInstructores = async () => {
  try {
    const requestBody = addAuthToRequestBody({});
    const response = await fetch(API_URL, {
      method: "GET"
    });
    console.log(response);
    return await response.json();
  } catch (error) {
    console.error("Error fetching all instructores:", error);
    throw error;
  }
};

export const getInstructorByCI = async (ci) => {
  try {
    const requestBody = addAuthToRequestBody({});
    const response = await fetch(`${API_URL}/${ci}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });

    return await response.json();
  } catch (error) {
    console.error(`Error fetching instructor with CI ${ci}:`, error);
    throw error;
  }
};

export const createInstructor = async (instructorData) => {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(instructorData),
    });
    return await response.json();
  } catch (error) {
    console.error("Error creating instructor:", error);
    throw error;
  }
};

export const updateInstructor = async (ci, instructorData) => {
  try {
    const requestBody = addAuthToRequestBody(instructorData);
    const response = await fetch(`${API_URL}/${ci}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });
    return await response.json();
  } catch (error) {
    console.error(`Error updating instructor with CI ${ci}:`, error);
    throw error;
  }
};

export const deleteInstructor = async (ci) => {
  try {
    const requestBody = addAuthToRequestBody({});

    const response = await fetch(`${API_URL}/${ci}`, {
      method: "DELETE",
      body: JSON.stringify(requestBody),
    });
    return await response.json();
  } catch (error) {
    console.error(`Error deleting instructor with CI ${ci}:`, error);
    throw error;
  }
};
