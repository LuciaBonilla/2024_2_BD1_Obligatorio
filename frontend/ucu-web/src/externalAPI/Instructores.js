import { createOptions } from "./AuthAuxiliar";

const API_URL = "http://localhost:3006/api/instructores";

export const getAllInstructores = async () => {
  try {
    const response = await fetch(API_URL, createOptions("GET"));
    return await response.json();
  } catch (error) {
    console.error("Error fetching all instructores:", error);
    throw error;
  }
};

export const getInstructorByCI = async (ci) => {
  try {
    const response = await fetch(`${API_URL}/${ci}`,createOptions("GET"));

    return await response.json();
  } catch (error) {
    console.error(`Error fetching instructor with CI ${ci}:`, error);
    throw error;
  }
};

export const createInstructor = async (instructorData) => {
  try {
    const response = await fetch(API_URL,createOptions("POST", instructorData));
    return await response.json();
  } catch (error) {
    console.error("Error creating instructor:", error);
    throw error;
  }
};

export const updateInstructor = async (ci, instructorData) => {
  try {
    const response = await fetch(`${API_URL}/${ci}`,createOptions("PATCH", instructorData));
    return await response.json();
  } catch (error) {
    console.error(`Error updating instructor with CI ${ci}:`, error);
    throw error;
  }
};

export const deleteInstructor = async (ci) => {
  try {

    const response = await fetch(`${API_URL}/${ci}`, createOptions("DELETE"));
    return await response.json();
  } catch (error) {
    console.error(`Error deleting instructor with CI ${ci}:`, error);
    throw error;
  }
};
