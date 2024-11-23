import axios from 'axios';

const API_BASE_URL = 'http://localhost:3006/api/instructores';

export const getAllInstructores = async () => {
  try {
    const response = await axios.get(API_BASE_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching instructores:', error);
    throw error;
  }
};

export const getInstructorByCI = async (ci) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/${ci}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching instructor with CI ${ci}:`, error);
    throw error;
  }
};

export const createInstructor = async (instructor) => {
  try {
    const response = await axios.post(API_BASE_URL, instructor);
    return response.data;
  } catch (error) {
    console.error('Error creating instructor:', error);
    throw error;
  }
};

export const updateInstructor = async (ci, instructor) => {
  try {
    const response = await axios.patch(`${API_BASE_URL}/${ci}`, instructor);
    return response.data;
  } catch (error) {
    console.error(`Error updating instructor with CI ${ci}:`, error);
    throw error;
  }
};

export const deleteInstructor = async (ci) => {
  try {
    const response = await axios.delete(`${API_BASE_URL}/${ci}`);
    return response.data;
  } catch (error) {
    console.error(`Error deleting instructor with CI ${ci}:`, error);
    throw error;
  }
};