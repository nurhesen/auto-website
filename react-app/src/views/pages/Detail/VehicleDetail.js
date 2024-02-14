import {
  Avatar,
  Box,
  Card,
  CardMedia,
  Chip,
  Divider,
  IconButton,
  Stack,
  Switch,
  Typography,
} from "@mui/material";

import { useState } from "react";

function VehicleDetail({ current }) {
  const [mainImage, setMainImage] = useState(0)
  return (
    <Card
      sx={{
        backgroundColor: "#362b358c",
        borderColor: "purple",
        borderWidth: "1px",
        borderStyle: "solid",
        color: "white",

      }}
    >
      <Box sx={{ p: 2, display: "flex" }}>
        <CardMedia
          component="img"
          image={process.env.REACT_APP_BASE_URL + current?.images[mainImage].image}
          alt="green iguana"
          className='main-image'
        />
      </Box>
      <Box
        sx={{
          display: "flex",
          overflowX: 'auto',
          mx: "1rem",
          '&::-webkit-scrollbar': {
            width: '12px',
          },
          '&::-webkit-scrollbar-track': {
            background: '#e1b6e1',
          },
          '&::-webkit-scrollbar-thumb': {
            background: 'purple', // Pink color for the scrollbar thumb
            borderRadius: '6px',
          },
          ">*": {
            width: "30%",
            mx: "0.5rem",
          },
        }}
      >
        {current?.images.map((data, ind) => (
          <CardMedia
            key={ind}
            className='card-scroll'
            component="img"
            image={process.env.REACT_APP_BASE_URL + data.image}
            onClick={() => setMainImage(ind)}
            alt="green iguana"
          />
        ))}
      </Box>

      <Divider />
      <Stack
        direction="column"
        alignItems="center"
        justifyContent="space-between"
        sx={{ px: 2, py: 1 }}
      >
        {[
          {
            name: "Title",
            value: current?.title,
          },
          {
            name: "Model",
            value: current?.brand_model,
          },
          {
            name: "Color",
            value: current?.color,
          },
          {
            name: "Vehicle",
            value: current?.vehicle_type,
          },
          {
            name: "Year",
            value: current?.year,
          },
          {
            name: "Price",
            value: current?.price + " " + current?.currency,
          },
          {
            name: "Km Traveled",
            value: current?.km_traveled + " km",
          },
          {
            name: "Fuel",
            value: current?.fuel,
          },
          {
            name: "Classification",
            value: current?.classification,
          },
        ].map((data, index) => (
          <Box
            key={index}
            sx={{
              display: "flex",
              justifyContent: "space-between",
              width: "100%",
              ">*": { mx: "1rem" },
            }}
          >
            <div>{data.name}:</div> <div>{data.value}</div>
          </Box>
        ))}
      </Stack>
    </Card>
  );
}

export default VehicleDetail;
