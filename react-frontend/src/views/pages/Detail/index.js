import { useDispatch, useSelector } from "react-redux";

import { useEffect } from "react";

import { useParams } from "react-router-dom";
import VehicleDetail from "./VehicleDetail";

import { getCurrentVehicleAction } from "../../../redux/actions/VehicleActions";
import CustomContainer from "../../components/CustomContainer";
import './style.scss';

function Detail() {
  const vehicleStore = useSelector((state) => state.vehicleStore);

  const params = useParams();
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getCurrentVehicleAction(params.id));
  }, []);

  return (
    <div className="detail-page">
      <CustomContainer>
        <VehicleDetail current={vehicleStore?.current} />
      </CustomContainer>
    </div>
  );
}

export default Detail;
