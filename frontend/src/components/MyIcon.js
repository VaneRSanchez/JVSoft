import React from 'react';
import { ReactComponent as MenuIcon } from '../assets/icons/menu.svg';

const icons = {
  'menu': MenuIcon
};

const MyIcon = ({ icon }) => {
  const MyIconComponent = icons[icon];

  if (!MyIconComponent) {
    return null;
  }

  return <MyIconComponent />;
};

export default MyIcon;
