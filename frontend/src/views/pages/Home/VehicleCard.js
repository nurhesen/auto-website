import * as React from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Typography from "@mui/material/Typography";
import { CardActionArea } from "@mui/material";
import { useNavigate } from "react-router-dom";

export default function VehicleCard({ vehicle }) {
  const navigate = useNavigate();
  return (
    <Card
      sx={{
        maxWidth: 345,
        backgroundColor: "#362b358c",
        borderColor: "purple",
        borderWidth: "1px",
        borderStyle: "solid",
      }}
      onClick={() => navigate("vehicles/" + vehicle.id, { replace: true })}
    >
      <CardActionArea sx={{ color: "white" }}>
        <CardMedia
          component="img"
          height="140"
          image={process.env.REACT_APP_BASE_URL + vehicle.image}
          alt="green iguana"
        />
        <CardContent>
          <Typography gutterBottom variant="h6" component="div">
            {vehicle.price + " " + vehicle.currency}
          </Typography>
          <Typography variant="body2">{vehicle.title}</Typography>
          <Typography variant="body2">{vehicle.brand_model}</Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}
