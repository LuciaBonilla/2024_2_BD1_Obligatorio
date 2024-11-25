const API_URL_CLASES = "http://localhost:3006/api/clases";

const addAuthToRequest = (body) => {
    return {
        ...body,
        correo: "admin@mail.com",
        contrasena: "123",
    };
};

export const getAllClases = async () => {
    try {
        const response = await fetch(API_URL_CLASES, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });
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
        const response = await fetch(`${API_URL_CLASES}/${id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });
        return await response.json();
    } catch (error) {
        console.error(`Error fetching clase with ID ${id}:`, error);
        throw error;
    }
};

export const createClase = async (clase) => {
    try {
        const requestBody = addAuthToRequest(clase);
        const response = await fetch(API_URL_CLASES, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(requestBody),
        });
        return await response.json();
    } catch (error) {
        console.error("Error creating clase:", error);
        throw error;
    }
};

export const updateClase = async (id, clase) => {
    try {
        const requestBody = addAuthToRequest(clase);
        const response = await fetch(`${API_URL_CLASES}/${id}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(requestBody),
        });
        return await response.json();
    } catch (error) {
        console.error(`Error updating clase with ID ${id}:`, error);
        throw error;
    }
};

export const deleteClase = async (id) => {
    try {
        const requestBody = addAuthToRequest({});
        const response = await fetch(`${API_URL_CLASES}/${id}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(requestBody),
        });
        return await response.json();
    } catch (error) {
        console.error(`Error deleting clase with ID ${id}:`, error);
        throw error;
    }
};