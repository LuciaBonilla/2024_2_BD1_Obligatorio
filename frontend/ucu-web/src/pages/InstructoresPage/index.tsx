import React, { useState, useEffect } from "react";
import {
  Container,
  Typography,
  Button,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  TextField,
} from "@mui/material";

import {
  getAllInstructores,
  createInstructor,
  updateInstructor,
  deleteInstructor,
} from "../../externalAPIs";

interface Instructor {
  ci: number;
  name: string;
  // Add other fields as necessary
}

const InstructoresPage: React.FC = () => {
  const [instructores, setInstructores] = useState<Instructor[]>([]);
  const [open, setOpen] = useState(false);
  const [currentInstructor, setCurrentInstructor] = useState<Instructor | null>(
    null
  );

  useEffect(() => {
    fetchInstructores();
  }, []);

  const fetchInstructores = async () => {
    const data = await getAllInstructores();
    setInstructores(data);
  };

  const handleOpen = (instructor: Instructor | null) => {
    setCurrentInstructor(instructor);
    setOpen(true);
  };

  const handleClose = () => {
    setCurrentInstructor(null);
    setOpen(false);
  };

  const handleSave = async () => {
    if (currentInstructor) {
      if (currentInstructor.ci) {
        await updateInstructor(currentInstructor.ci, currentInstructor);
      } else {
        await createInstructor(currentInstructor);
      }
      fetchInstructores();
      handleClose();
    }
  };

  const handleDelete = async (ci: number) => {
    await deleteInstructor(ci);
    fetchInstructores();
  };

  return <></>;
};

export default InstructoresPage;
