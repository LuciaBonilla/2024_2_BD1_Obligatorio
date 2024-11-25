import { createOptions } from "./AuthAuxiliar";
const API_URL_CLASES = "http://localhost:3006/api/clases";


export const getAllClases = async () => {
  try {
    const response = await fetch(API_URL_CLASES, createOptions("GET"));
    if (response.status === 404) {
      return [];
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching all clases:", error);
    throw error;
  }
};

export const getClaseById = async (id) => {
  try {
    const response = await fetch(
      `${API_URL_CLASES}/${id}`,
      createOptions("GET")
    );
    return await response.json();
  } catch (error) {
    console.error(`Error fetching clase with ID ${id}:`, error);
    throw error;
  }
};

export const createClase = async (clase) => {
  try {
    const response = await fetch(API_URL_CLASES, createOptions("POST", clase));
    return await response.json();
  } catch (error) {
    console.error("Error creating clase:", error);
    throw error;
  }
};

export const updateClase = async (id, clase) => {
  try {
    const response = await fetch(
      `${API_URL_CLASES}/${id}`,
      createOptions("PATCH", clase)
    );
    return await response.json();
  } catch (error) {
    console.error(`Error updating clase with ID ${id}:`, error);
    throw error;
  }
};

export const deleteClase = async (id) => {
  try {
    const response = await fetch(
      `${API_URL_CLASES}/${id}`,
      createOptions("DELETE")
    );
    return await response.json();
  } catch (error) {
    console.error(`Error deleting clase with ID ${id}:`, error);
    throw error;
  }
};
