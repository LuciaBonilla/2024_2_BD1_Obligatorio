const API_URL_ALUMNOS = "http://localhost:3006/api/alumnos";
import { createOptions } from "./AuthAuxiliar";

export const getAllAlumnos = async () => {
  try {
    const response = await fetch(API_URL_ALUMNOS, createOptions("GET"));
    if (response.status === 404) {
      return [];
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching all alumnos:", error);
    throw error;
  }
};

export const getAlumnoByCI = async (ci) => {
  try {
    const response = await fetch(
      `${API_URL_ALUMNOS}/${ci}`,
      createOptions("GET")
    );
    return await response.json();
  } catch (error) {
    console.error(`Error fetching alumno with CI ${ci}:`, error);
    throw error;
  }
};

export const createAlumno = async (alumno) => {
  try {
    const response = await fetch(
      API_URL_ALUMNOS,
      createOptions("POST", alumno)
    );
    return await response.json();
  } catch (error) {
    console.error("Error creating alumno:", error);
    throw error;
  }
};

export const updateAlumno = async (ci, alumno) => {
  try {
    const response = await fetch(
      `${API_URL_ALUMNOS}/${ci}`,
      createOptions("PATCH", alumno)
    );
    return await response.json();
  } catch (error) {
    console.error(`Error updating alumno with CI ${ci}:`, error);
    throw error;
  }
};

export const deleteAlumno = async (ci) => {
  try {
    const response = await fetch(
      `${API_URL_ALUMNOS}/${ci}`,
      createOptions("DELETE")
    );
    return await response.json();
  } catch (error) {
    console.error(`Error deleting alumno with CI ${ci}:`, error);
    throw error;
  }
};
