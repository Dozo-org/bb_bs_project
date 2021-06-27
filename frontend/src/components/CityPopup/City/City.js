import React from 'react';
import './City.css';

const City= React.memo((props) => {
  const {id, city, handleChange} = props;

  return (
    <li className="cities-list__item" onClick={() => handleChange(id)}>
      {city}
    </li>
  )}
)

export default City;