import styled from 'styled-components'

const ButtonSave = styled.button({
    cursor: 'pointer',
    background: 'transparent',
    fontSize: '16px',
    borderRadius: '16px',
    fontWeight: 'bold',
    color: 'green',
    border: '2px solid green',
    margin: '0 1em',
    padding: '0.25em 1em',
    transition: '0.5s all ease-out',
    '&: hover': {
        backgroundColor: 'green',
        color: 'white',
    }
})

export default ButtonSave;