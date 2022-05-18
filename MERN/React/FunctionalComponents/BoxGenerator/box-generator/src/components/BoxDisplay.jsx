import React, {useState} from 'react';
import styled from 'styled-components';

const BoxDisplay = styled.div`
    background: ${props => props.bgColor};
    width: ${props => props.width || '40px'};
    height: ${props => props.height || '40px'};
    `;

export default BoxDisplay;