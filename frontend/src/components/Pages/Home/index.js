import React, { useState, useEffect } from 'react';
import ButtonDelete from '../../Atoms/ButtonDelete'
import ButtonEdit from '../../Atoms/ButtonEdit'
import ButtonSave from '../../Atoms/ButtonSave'
import CardRecipe from '../../Molecules/CardRecipe'
import CardCashier from '../../Molecules/CardCashier'
import CardExpenditure from '../../Molecules/CardExpenditure'
import user from '../../../assets/user.jpg'
import { FaWallet, FaCashRegister, FaMoneyBillWave } from 'react-icons/fa'
import api from '../../../services/api'

export default function Home({ }) {
    const [launch, setLaunch] = useState([])

    async function getLaunch() {
        const response = await api.get('launchs')
            .then((res) => {
                setLaunch(res)
                console.log("RESPONSE: ", res)
            })
            .catch((err) => {
                console.log(err)
            })
    }

    useEffect(() => {
        getLaunch()
    }, [])


    return (
        <div style={{
            display: 'flex',
            flexDirection: 'column',
            minHeight: '100vh',
        }}>
            <div>
                <p>Olá usuário</p>
                <img style={{ borderRadius: '50px' }} src={user}></img>
            </div>
            <div
                style={{
                    display: 'flex',
                    flexDirection: 'row',
                    height: '100vh'
                }}>
                <div style={{ backgroundColor: 'gray', width: '20%', height: 'auto' }}>
                    <ButtonDelete>DELETE</ButtonDelete>
                    <ButtonEdit>EDIT</ButtonEdit>
                    <ButtonSave>SAVE</ButtonSave>
                </div>
                <div style={{
                    width: '80%'
                }}>
                    <div style={{
                        display: 'flex', flexDirection: 'row',
                        justifyContent: 'space-between',
                        alignItems: 'center'
                    }}>
                        <CardRecipe>
                            <div>
                                <strong style={{ color: 'white', fontSize: '2em' }}>R$2900,00</strong>
                                <p style={{ color: 'white', marginTop: '.4em' }}>Total de Receitas</p>
                            </div>
                            <FaCashRegister style={{ color: 'white', fontSize: '3em' }} />
                        </CardRecipe>
                        <CardExpenditure >
                            <div>
                                <strong style={{ color: 'white', fontSize: '2em' }}>R$ {console.log("launch: ", launch)}</strong>
                                <p style={{ color: 'white', marginTop: '.4em' }}>Total de Despesas</p>
                            </div>
                            <FaWallet style={{ color: 'white', fontSize: '3em' }} />
                        </CardExpenditure>
                        <CardCashier>
                            <div>
                                <strong style={{ color: 'white', fontSize: '2em' }}>R$400,00</strong>
                                <p style={{ color: 'white', marginTop: '.4em' }}>Caixa atual</p>
                            </div>
                            <FaMoneyBillWave style={{ color: 'white', fontSize: '3em' }} />
                        </CardCashier>
                    </div>

                </div>
            </div>
        </div >
    )
}