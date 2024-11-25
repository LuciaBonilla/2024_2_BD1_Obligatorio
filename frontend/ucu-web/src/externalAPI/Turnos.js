import { createOptions } from "./AuthAuxiliar";

const API_URL = "http://localhost:3006/api/turnos";

export const getAllTurnos = async () => {
  try {
    const response = await fetch(API_URL, createOptions("GET"));
    return await response.json();
  } catch (error) {
    console.error("Error fetching all turnos:", error);
    throw error;
  }
};

export const getTurnoById = async (id) => {
  try {
    const response = await fetch(`${API_URL}/${id}`, createOptions("GET"));
    return await response.json();
  } catch (error) {
    console.error(`Error fetching turno with id ${id}:`, error);
    throw error;
  }
};

export const createTurno = async (turno) => {
  try {
    const response = await fetch(API_URL, createOptions("POST", turno));
    return await response.json();
  } catch (error) {
    console.error("Error creating turno:", error);
    throw error;
  }
};

export const updateTurno = async (id, turno) => {
  try {
    const response = await fetch(
      `${API_URL}/${id}`,
      createOptions("PATCH", turno)
    );
    return await response.json();
  } catch (error) {
    console.error(`Error updating turno with id ${id}:`, error);
    throw error;
  }
};

export const deleteTurno = async (id) => {
  try {
    const response = await fetch(`${API_URL}/${id}`, createOptions("DELETE"));
    return await response.json();
  } catch (error) {
    console.error(`Error deleting turno with id ${id}:`, error);
    throw error;
  }
};
