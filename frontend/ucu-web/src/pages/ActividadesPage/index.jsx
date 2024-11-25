import React, { useState, useEffect } from "react";
import { Box, Button, Stack, TextField } from "@mui/material";
import {
  getAllActividades,
  updateActividad,
  deleteActividad,
} from "../../externalAPI/Actividades";
import DataTable from "../../components/DataTable";

const ActividadesPage = () => {
  const [actividades, setActividades] = useState([]);
  const [form, setForm] = useState({
    id: null,
    nombre: "",
    descripcion: "",
    costo: "",
    edad_minima: "",
  });
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    getAllActividades().then((actividades) => setActividades(actividades));
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isEditing) {
      updateActividad(form.id, form).then(() => {
        getAllActividades().then((actividades) => setActividades(actividades));
        setIsEditing(false);
        setForm({
          id: null,
          nombre: "",
          descripcion: "",
          costo: "",
          edad_minima: "",
        });
      });
    }
  };

  const handleEdit = (actividad) => {
    setForm(actividad);
    setIsEditing(true);
  };

  const handleDelete = (deleteActividad) => {
    deleteActividad(deleteActividad.id).then(() => {
      setActividades((prev) =>
        prev.filter((actividad) => actividad.id !== deleteActividad.id)
      );
    });
  };

  return (
    <Box>
      <Stack spacing={1}>
        <DataTable
          data={actividades}
          onEdit={handleEdit}
          onDelete={handleDelete}
        />
        <form onSubmit={handleSubmit}>
          <Stack spacing={2}>
            <TextField
              label="Nombre"
              name="nombre"
              value={form.nombre}
              onChange={handleInputChange}
            />
            <TextField
              label="Descripción"
              name="descripcion"
              value={form.descripcion}
              onChange={handleInputChange}
            />
            <TextField
              label="Costo"
              name="costo"
              value={form.costo}
              type="number"
              onChange={handleInputChange}
            />
            <TextField
              label="Edad Mínima"
              name="edad_minima"
              value={form.edad_minima}
              type="number"
              onChange={handleInputChange}
            />
            <Button type="submit">{"Actualizar"}</Button>
          </Stack>
        </form>
      </Stack>
    </Box>
  );
};

export default ActividadesPage;
