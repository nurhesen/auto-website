import { useDispatch, useSelector } from "react-redux";

import { Box } from "@mui/system";

import Input from "@mui/material/Input";
import InputAdornment from "@mui/material/InputAdornment";
import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import Button from "@mui/material/Button";

import Select from "@mui/material/Select";
import {
  getVehiclesAction,
  searchFormChange,
} from "../../../redux/actions/VehicleActions";
import Autocomplete from "@mui/material/Autocomplete";
import TextField from "@mui/material/TextField";

function SearchVehicle() {
  const searchForm = useSelector((state) => state.searchForm);
  const brands = useSelector((state) => state.brandStore.data);

  const dispatch = useDispatch();

  const onInputChange = (name) => {
    return (e) => {
      const val = e.target.value || e.target.textContent;
      dispatch(searchFormChange({ [name]: val }));
    };
  };

  return (
    <>
      <Box
        sx={{
          display: "flex",
        }}
      >
        <Autocomplete
          freeSolo
          disablePortal
          options={brands || []}
          sx={{ width: 300 }}
          value={searchForm.brand || ""}
          onChange={onInputChange("brand")}
          renderInput={(params) => (
            <TextField
              {...params}
              onChange={onInputChange("model")}
              label="Brand"
            />
          )}
        />
        <Autocomplete
          freeSolo
          disablePortal
          options={[]}
          sx={{ width: 300 }}
          value={searchForm.model || ""}
          onChange={onInputChange("model")}
          renderInput={(params) => (
            <TextField
              {...params}
              onChange={onInputChange("model")}
              label="Model"
            />
          )}
        />
      </Box>
      <Box
        sx={{
          display: "flex",
        }}
      >
        <Autocomplete
          freeSolo
          disablePortal
          options={[...Array(28).keys()].map((d) => `${1995 + d}`)}
          sx={{ width: 300 }}
          value={searchForm.min_year || ""}
          onChange={onInputChange("min_year")}
          renderInput={(params) => <TextField {...params} label="Min Year" />}
        />
        <Autocomplete
          freeSolo
          disablePortal
          options={[...Array(28).keys()].map((d) => `${1995 + d}`)}
          sx={{ width: 300 }}
          value={searchForm.max_year || ""}
          onChange={onInputChange("max_year")}
          renderInput={(params) => (
            <TextField
              {...params}
              onChange={(e) => {
                console.log("fdsafsda", e);
              }}
              label="Max Year"
            />
          )}
        />
      </Box>
      <Box
        sx={{
          display: "flex",
          ">*": { width: "100%", mx: "1.05rem" },
        }}
      >
        <FormControl fullWidth sx={{ m: 1 }} variant="standard">
          <InputLabel htmlFor="standard-adornment-amount">Min Price</InputLabel>
          <Input
            id="standard-adornment-amount"
            value={searchForm.min_price || ""}
            onChange={onInputChange("min_price")}
            startAdornment={<InputAdornment position="start">$</InputAdornment>}
          />
        </FormControl>
        <FormControl fullWidth sx={{ m: 1 }} variant="standard">
          <InputLabel htmlFor="standard-adornment-amount">Max Price</InputLabel>
          <Input
            id="standard-adornment-amount"
            value={searchForm.max_price || ""}
            onChange={onInputChange("max_price")}
            startAdornment={<InputAdornment position="start">$</InputAdornment>}
          />
        </FormControl>
      </Box>
      <Box
        sx={{
          display: "flex",
          ">*": { width: "100%", mx: "1.05rem" },
        }}
      >
        <FormControl fullWidth sx={{ m: 1 }} variant="standard">
          <InputLabel htmlFor="standard-adornment-amount">Min Km</InputLabel>
          <Input
            id="standard-adornment-amount"
            value={searchForm.min_km_traveled || ""}
            onChange={onInputChange("min_km_traveled")}
            startAdornment={
              <InputAdornment position="start">Km</InputAdornment>
            }
          />
        </FormControl>
        <FormControl fullWidth sx={{ m: 1 }} variant="standard">
          <InputLabel htmlFor="standard-adornment-amount">Max Km</InputLabel>
          <Input
            id="standard-adornment-amount"
            value={searchForm.max_km_traveled || ""}
            onChange={onInputChange("max_km_traveled")}
            startAdornment={
              <InputAdornment position="start">Km</InputAdornment>
            }
          />
        </FormControl>
      </Box>

      <Box
        sx={{
          display: "flex",
          ">*": { width: "95%", mx: "auto" },
        }}
      >
        <FormControl fullWidth variant="standard">
          <InputLabel htmlFor="standard-adornment-amount">Color</InputLabel>
          <Input
            id="standard-adornment-amount"
            value={searchForm.color || ""}
            onChange={onInputChange("color")}
          />
        </FormControl>
      </Box>
      <Box
        sx={{
          display: "flex",
          ">*": { width: "50%" },
        }}
      >
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">Condition</InputLabel>
          <Select
            value={searchForm.condition || ""}
            label="Condition"
            onChange={onInputChange("condition")}
          >
            <MenuItem value={""}>All</MenuItem>
            <MenuItem value={1}>New</MenuItem>
            <MenuItem value={2}>Used</MenuItem>
          </Select>
        </FormControl>

        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">Fuel</InputLabel>
          <Select
            value={searchForm.fuel || ""}
            label="Fuel"
            onChange={onInputChange("fuel")}
          >
            <MenuItem value={""}>All</MenuItem>
            <MenuItem value={1}>Gasoline</MenuItem>
            <MenuItem value={2}>Diesel</MenuItem>
            <MenuItem value={3}>Gas</MenuItem>
            <MenuItem value={4}>Electro</MenuItem>
            <MenuItem value={5}>Hybrid</MenuItem>
          </Select>
        </FormControl>
      </Box>
      <Box
        sx={{
          display: "flex",
          ">*": { width: "50%" },
        }}
      >
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">Vehicle type</InputLabel>
          <Select
            value={searchForm.vehicle_type || ""}
            label="Vehicle type"
            onChange={onInputChange("vehicle_type")}
          >
            <MenuItem value={""}>All</MenuItem>
            <MenuItem value={1}>Car</MenuItem>
            <MenuItem value={2}>Motorcycle</MenuItem>
          </Select>
        </FormControl>

        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">Classification</InputLabel>
          <Select
            value={searchForm.classification || ""}
            label="Classification"
            onChange={onInputChange("classification")}
          >
            <MenuItem value={""}>All</MenuItem>
            <MenuItem value={1}>Modern</MenuItem>
            <MenuItem value={2}>Classic</MenuItem>
            <MenuItem value={3}>Antique</MenuItem>
            <MenuItem value={4}>Vintage</MenuItem>
          </Select>
        </FormControl>
      </Box>

      <Button
        variant="contained"
        color="secondary"
        sx={{
          background: "linear-gradient(45deg, violet, purple, violet)",
          width: "100%",
        }}
        onClick={() => dispatch(getVehiclesAction)}
      >
        Search Vehicles
      </Button>
    </>
  );
}

export default SearchVehicle;
