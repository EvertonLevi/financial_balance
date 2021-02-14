import styled from 'styled-components'

const TitleCardRecipe = styled.p({

})

const IconCardRecipe = styled.img({

})

const SutTitle = styled.span({

})

const Value = styled.h2({

})

const CardRecipe = styled.div({
    overflow: 'hidden',
    padding: '0 0 0 0',
    margin: '48px auto 0px',
    width: '300px',
    display: 'flex', 
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
    //TODO height: 'auto' depois dos testes
    height: '120px',
    boxShadow: '0 0 20px rgba(0, 0, 0, 0.2), 0 0px 40px rgba(0, 0, 0, 0.08)',
    borderRadius: '5px',
    background: 'linear-gradient(4.5rad, #4ED647, #7BD647, #4ED647, #52F77A)',
})

export default CardRecipe;
