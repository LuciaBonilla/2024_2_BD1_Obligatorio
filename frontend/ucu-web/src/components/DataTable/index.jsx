import React from 'react';
import PropTypes from 'prop-types';
import { DataGrid } from '@mui/x-data-grid';
import { Button, Stack } from '@mui/material';

const DataTable = ({ data, onEdit, onDelete }) => {
  if (!data || data.length === 0) {
    return <div>No data available</div>;
  }

  const columns = Object.keys(data[0]).map((key) => ({
    field: key,
    headerName: key.charAt(0).toUpperCase() + key.slice(1),
    width: 150,
  }));

  // Add a new column for the actions (edit and delete buttons)
  columns.push({
    field: 'actions',
    headerName: 'Actions',
    width: 150,
    renderCell: (params) => (
      <Stack direction="row" spacing={1}>
        <Button onClick={() => onEdit(params.row)}>📝</Button>
        <Button onClick={() => onDelete(params.row)}>🗑️</Button>
      </Stack>
    ),
  });

  const rows = data.map((item, index) => ({ id: index, ...item }));

  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid rows={rows} columns={columns} pageSize={5} />
    </div>
  );
};

DataTable.propTypes = {
  data: PropTypes.arrayOf(PropTypes.object).isRequired,
  onEdit: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
};

export default DataTable;
