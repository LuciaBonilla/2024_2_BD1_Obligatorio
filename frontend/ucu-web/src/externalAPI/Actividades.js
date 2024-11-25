import { createOptions } from "./AuthAuxiliar";

const API_URL = "http://localhost:3006/api/actividades";

export const getAllActividades = async () => {
  try {
    const response = await fetch(API_URL, createOptions("GET"));
    return await response.json();
  } catch (error) {
    console.error("Error fetching all actividades:", error);
    throw error;
  }
};

export const getActividadById = async (id) => {
  try {
    const response = await fetch(`${API_URL}/${id}`, createOptions("GET"));
    return await response.json();
  } catch (error) {
    console.error(`Error fetching actividad with id ${id}:`, error);
    throw error;
  }
};

export const updateActividad = async (id, actividad) => {
  try {
    const response = await fetch(
      `${API_URL}/${id}`,
      createOptions("PATCH", actividad)
    );
    return await response.json();
  } catch (error) {
    console.error(`Error updating actividad with id ${id}:`, error);
    throw error;
  }
};

export const deleteActividad = async (id) => {
  try {
    const response = await fetch(`${API_URL}/${id}`, createOptions("DELETE"));
    return await response.json();
  } catch (error) {
    console.error(`Error deleting actividad with id ${id}:`, error);
    throw error;
  }
};
