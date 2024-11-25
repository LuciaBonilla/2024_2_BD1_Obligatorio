import React, { useState, useEffect } from "react";
import { Box, Button, Stack, TextField } from "@mui/material";
import {
  getAllTurnos,
  createTurno,
  updateTurno,
  deleteTurno,
} from "../../externalAPI/Turnos";
import DataTable from "../../components/DataTable";

const TurnosPage = () => {
  const [turnos, setTurnos] = useState([]);
  const [form, setForm] = useState({
    id: null,
    hora_fin: "",
    hora_inicio: "",
  });
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    getAllTurnos().then((turnos) => setTurnos(turnos));
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isEditing) {
      updateTurno(form.id, form).then(() => {
        setTurnos((prev) =>
          prev.map((turno) => (turno.id === form.id ? form : turno))
        );
        setIsEditing(false);
        setForm({
          id: null,
          hora_fin: "",
          hora_inicio: "",
        });
      });
    } else {
      createTurno(form).then(() => {
        getAllTurnos().then((turnos) => setTurnos(turnos));
        setForm({
          id: null,
          hora_fin: "",
          hora_inicio: "",
        });
      });
    }
  };

  const handleEdit = (turno) => {
    setForm(turno);
    setIsEditing(true);
  };

  const handleDelete = (deletTurno) => {
    deleteTurno(deletTurno.id).then(() => {
      setTurnos((prev) => prev.filter((turno) => turno.id !== deletTurno.id));
    });
  };

  return (
    <Box>
      <Stack spacing={1}>
        <DataTable data={turnos} onEdit={handleEdit} onDelete={handleDelete} />
        <form onSubmit={handleSubmit}>
          <Stack spacing={2}>
            <TextField
              label="Hora de inicio"
              name="hora_inicio"
              value={form.hora_inicio}
              type="time"
              onChange={handleInputChange}
            />
            <TextField
              label="Hora de finalización"
              name="hora_fin"
              value={form.hora_fin}
              type="time"
              onChange={handleInputChange}
            />
            <Button type="submit">{isEditing ? "Actualizar" : "Crear"}</Button>
          </Stack>
        </form>
      </Stack>
    </Box>
  );
};

export default TurnosPage;
