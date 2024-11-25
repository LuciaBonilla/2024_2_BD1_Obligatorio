import React, { useState, useEffect } from "react";
import { Box, Button, Stack, TextField } from "@mui/material";
import {
  getAllClases,
  createClase,
  updateClase,
  deleteClase,
} from "../../externalAPI/Clases";
import DataTable from "../../components/DataTable";

const ClasesPage = () => {
  const [clases, setClases] = useState([]);
  const [form, setForm] = useState({
    id: null,
    ci_instructor: "",
    id_turno: "",
    id_actividad: "",
    dictada: "",
  });
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    getAllClases().then((clases) => setClases(clases));
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isEditing) {
      updateClase(form.id, form).then(() => {
        setClases((prev) =>
          prev.map((clase) => (clase.id === form.id ? form : clase))
        );
        setIsEditing(false);
        setForm({
          id: null,
          ci_instructor: "",
          id_turno: "",
          id_actividad: "",
          dictada: "",
        });
      });
    } else {
      createClase(form).then(() => {
        getAllClases().then((clases) => setClases(clases));
        setForm({
          ci_instructor: "",
          id_turno: "",
          id_actividad: "",
          dictada: "",
        });
      });
    }
  };

  const handleEdit = (clase) => {
    setForm(clase);
    setIsEditing(true);
  };

  const handleDelete = (toDeleteClase) => {
    deleteClase(toDeleteClase.id).then(() => {
      setClases((prev) => prev.filter((clase) => clase.id !== toDeleteClase.id));
    });
  };

  return (
    <dic>
      <Box>
        <DataTable data={clases} onEdit={handleEdit} onDelete={handleDelete} />
        <h2>{isEditing ? "Editar Clase" : "Crear Clase"}</h2>
        <form onSubmit={handleSubmit}>
          <Stack spacing={2}>
            <TextField
              label="Cedula Instructor"
              name="ci_instructor"
              value={form.ci_instructor}
              onChange={handleInputChange}
            />
            <TextField
              label="Id de Actividad"
              name="id_actividad"
              value={form.id_actividad}
              onChange={handleInputChange}
            />
            <TextField
              label="Id Turno"
              name="id_turno"
              value={form.id}
              onChange={handleInputChange}
            />
            <TextField
              label="Fue dictada?"
              name="dictada"
              value={form.dictada}
              onChange={handleInputChange}
            />
            <Button type="submit">{isEditing ? "Actualizar" : "Crear"}</Button>
          </Stack>
        </form>
      </Box>
    </dic>
  );
};

export default ClasesPage;
