import "./Tag.css";
import React from "react";

function Tag(props) {
  const [isSelected, setIsSelected] = React.useState(false);

  const handleTagClick = () => {
    setIsSelected(!isSelected);
  };

  return (
    <li className="filters__item">
      <button
        type="button"
        onClick={handleTagClick}
        className={`filters__button ${
          isSelected ? "filters__button_active" : " "
        }`}
      >
        {props.name}
      </button>
    </li>
  );
}

export default Tag;
