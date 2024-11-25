import React, { useEffect, useState } from "react";
import {
  Container,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  CircularProgress,
  Alert,
} from "@mui/material";
import axios from "axios";
import { createOptions } from "../../externalAPI/AuthAuxiliar";
const ReportsPage = () => {
  const [mostProfitableActivities, setMostProfitableActivities] = useState([]);
  const [mostPopulateSchedules, setMostPopulateSchedules] = useState([]);
  const [mostPopulateActivities, setMostPopulateActivities] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [profitableActivities, populateSchedules, populateActivities] =
          await Promise.all([
            axios.get(
              "http://localhost:3006/api/reportes/actividades_mas_ingresos",
              createOptions("GET")
            ),
            axios.get(
              "http://localhost:3006/api/reportes/turnos_mas_frecuentes",
              createOptions("GET")
            ),
            axios.get(
              "http://localhost:3006/api/reportes/actividades_mas_alumnos",
              createOptions("GET")
            ),
          ]);

        setMostProfitableActivities(profitableActivities.data);
        setMostPopulateSchedules(populateSchedules.data);
        setMostPopulateActivities(populateActivities.data);
      } catch (error) {
        console.error("Error fetching data:", error);
        setError(error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  if (isLoading) {
    return (
      <Container>
        <CircularProgress />
      </Container>
    );
  }
  if (error) {
    return (
      <Container>
        <Alert severity="error">Error fetching data: {error.message}</Alert>
      </Container>
    );
  }
  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Reports
      </Typography>

      <Typography variant="h6" gutterBottom>
        Actividades más ingresos
      </Typography>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Actividad</TableCell>
              <TableCell>Profits Without Equipment</TableCell>
              <TableCell>Profits From Equipment</TableCell>
              <TableCell>Total Profits</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {mostProfitableActivities.map((activity, index) => (
              <TableRow key={index}>
                <TableCell>{activity.actividad}</TableCell>
                <TableCell>{activity.ganancias_sin_equipamiento}</TableCell>
                <TableCell>{activity.ganancias_por_equipamiento}</TableCell>
                <TableCell>{activity.ganancias_totales}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      <Typography variant="h6" gutterBottom>
        Turnos con más clases dictadas
      </Typography>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Schedule ID</TableCell>
              <TableCell>Start Time</TableCell>
              <TableCell>End Time</TableCell>
              <TableCell>Number of Classes</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {mostPopulateSchedules.map((schedule, index) => (
              <TableRow key={index}>
                <TableCell>{schedule.id_turno}</TableCell>
                <TableCell>{schedule.hora_inicio}</TableCell>
                <TableCell>{schedule.hora_fin}</TableCell>
                <TableCell>{schedule.num_clases_dictadas}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      <Typography variant="h6" gutterBottom>
        Actividades más alumnos
      </Typography>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Activity</TableCell>
              <TableCell>Number of Students</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {mostPopulateActivities.map((activity, index) => (
              <TableRow key={index}>
                <TableCell>{activity.actividad}</TableCell>
                <TableCell>{activity.num_alumnos_participantes}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
};

export default ReportsPage;
