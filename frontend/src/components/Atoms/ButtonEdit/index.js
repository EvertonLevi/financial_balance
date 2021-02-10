import styled from 'styled-components'

const ButtonEdit = styled.button({
    cursor: 'pointer',
    background: 'transparent',
    fontSize: '16px',
    borderRadius: '16px',
    fontWeight: 'bold',
    color: 'gray',
    border: '2px solid gray',
    margin: '0 1em',
    padding: '0.25em 1em',
    transition: '0.5s all ease-out',
    '&: hover': {
        backgroundColor: 'gray',
        color: 'white',
    }
})

export default ButtonEdit;