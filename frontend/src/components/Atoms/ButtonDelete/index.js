import styled from 'styled-components'

const ButtonDelete = styled.button({
    cursor: 'pointer',
    background: 'transparent',
    fontSize: '16px',
    borderRadius: '16px',
    fontWeight: 'bold',
    color: 'red',
    border: '2px solid red',
    margin: '0 1em',
    padding: '0.25em 1em',
    transition: '0.5s all ease-out',
    '&: hover': {
        backgroundColor: 'red',
        color: 'white',
    }
})

export default ButtonDelete;