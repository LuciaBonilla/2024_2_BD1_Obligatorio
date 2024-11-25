import React, { useState, useEffect } from "react";
import { Box, Button, Stack, TextField } from "@mui/material";
import {
  getAllAlumnos,
  createAlumno,
  updateAlumno,
  deleteAlumno,
} from "../../externalAPI/Estudiantes";
import DataTable from "../../components/DataTable";

const EstudiantesPage = () => {
  const [alumnos, setAlumnos] = useState([]);
  const [form, setForm] = useState({
    ci: null,
    nombre: "",
    apellido: "",
    fecha_nacimiento: "",
    telefono_contacto: "",
    correo_contacto: "",
  });
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    getAllAlumnos().then((alumnos) => setAlumnos(alumnos));
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isEditing) {
      updateAlumno(form.ci, form).then(() => {
        setAlumnos((prev) =>
          prev.map((alumno) => (alumno.ci === form.ci ? form : alumno))
        );
        resetForm();
      });
    } else {
      createAlumno(form).then((newAlumno) => {
        setAlumnos((prev) => [...prev, newAlumno]);
        resetForm();
      });
    }
  };

  const handleEdit = (alumno) => {
    setForm(alumno);
    setIsEditing(true);
  };

  const handleDelete = (alumno) => {
    deleteAlumno(alumno.ci).then(() => {
      setAlumnos((prev) => prev.filter((item) => item.ci !== alumno.ci));
    });
  };

  const resetForm = () => {
    setForm({
      ci: null,
      nombre: "",
      apellido: "",
      fecha_nacimiento: "",
      telefono_contacto: "",
      correo_contacto: "",
    });
    setIsEditing(false);
  };

  return (
    <>
      <DataTable data={alumnos} onEdit={handleEdit} onDelete={handleDelete} />
      <h2>{isEditing ? "Editar Alumno" : "Crear Alumno"}</h2>
      <Box component="form" onSubmit={handleSubmit}>
        <Stack spacing={1}>
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
            id="fecha_nacimiento"
            name="fecha_nacimiento"
            type="date"
            value={form.fecha_nacimiento}
            onChange={handleInputChange}
            inputLabel={{
              shrink: true,
            }}
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
        <Button type="submit">{isEditing ? "Actualizar" : "Crear"}</Button>
      </Box>
    </>
  );
};

export default EstudiantesPage;
