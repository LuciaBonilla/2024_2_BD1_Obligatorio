import React, { useState, useEffect } from 'react';
import { Box, Button, Stack, TextField } from '@mui/material';
import { getAllInstructores, createInstructor, updateInstructor, deleteInstructor } from '../../externalAPI/Instructores'; 
import DataTable from '../../components/DataTable'; 

const InstructoresPage = () => {
  const [instructores, setInstructores] = useState([]);
  const [form, setForm] = useState({
    ci: null,
    nombre: '',
    apellido: '',
    telefono_contacto: '',
    correo_contacto: '',
  });
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    getAllInstructores().then((instructores) => setInstructores(instructores));
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isEditing) {
      updateInstructor(form.ci, form).then(() => {
        setInstructores((prev) =>
          prev.map((instructor) =>
            instructor.ci === form.ci ? form : instructor
          )
        );
        resetForm();
      });
    } else {
      createInstructor(form).then(() => {
        setInstructores((prev) => [...prev, form]);
        resetForm();
      });
    }
  };

  const handleEdit = (instructor) => {
    setForm(instructor);
    setIsEditing(true);
  };

  const handleDelete = (instructor) => {
    deleteInstructor(instructor.ci).then(() => {
      setInstructores((prev) =>
        prev.filter((item) => item.ci !== instructor.ci)
      );
    });
  };

  const resetForm = () => {
    setForm({
      ci: null,
      nombre: "",
      apellido: "",
      telefono_contacto: "",
      correo_contacto: "",
    });
    setIsEditing(false);
  };

  return (
    <div>
      <h1>Instructores</h1>
      <DataTable data={instructores} onEdit={handleEdit} onDelete={handleDelete} />
      <h2>{isEditing ? "Editar Instructor" : "Crear Instructor"}</h2>
      <Box component="form" onSubmit={handleSubmit}>
        <Stack spacing={1} sx={{ width: "60%" }}>
          <TextField
            id="ci"
            name="ci"
            label="CI"
            value={form.ci || ""}
            onChange={handleInputChange}
            required
          />
          <TextField
            id="nombre"
            name="nombre"
            label="Nombre"
            value={form.nombre}
            onChange={handleInputChange}
            required
          />
          <TextField
            id="apellido"
            name="apellido"
            label="Apellido"
            value={form.apellido}
            onChange={handleInputChange}
            required
          />
          <TextField
            id="telefono_contacto"
            name="telefono_contacto"
            label="Teléfono de Contacto"
            value={form.telefono_contacto}
            onChange={handleInputChange}
            required
          />
          <TextField
            id="correo_contacto"
            name="correo_contacto"
            label="Correo de Contacto"
            value={form.correo_contacto}
            onChange={handleInputChange}
          />
        </Stack>
        <Button type="submit">{isEditing ? 'Actualizar' : 'Crear'}</Button>
      </Box>
    </div>
  );
};

export default InstructoresPage;
