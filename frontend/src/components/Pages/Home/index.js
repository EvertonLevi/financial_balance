import React from 'react';
import ButtonDelete from '../../Atoms/ButtonDelete'
import ButtonEdit from '../../Atoms/ButtonEdit'
import ButtonSave from '../../Atoms/ButtonSave'
import Card from '../../Molecules/Card'
import user from '../../../assets/user.jpg'

export default function Home({ }) {
    return (
        <div>
            <div>
                <h4>Olá usuário</h4>
                <img style={{borderRadius: '50px'}} src={user}></img>
            </div>
            {/* <div>
                <ButtonDelete>DELETE</ButtonDelete>
                <ButtonEdit>EDIT</ButtonEdit>
                <ButtonSave>SAVE</ButtonSave>
            </div> */}
            <div>
                <div>
                    <Card></Card>
                </div>
            </div>
        </div>
    )
}