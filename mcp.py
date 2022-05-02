#Credenciales de producción

    #Public Key
    #APP_USR-feab2ce0-24af-4c4b-ae29-f681fdc21ee8

    #Access token
    #APP_USR-4708051638906536-030215-5b711cad32b12099b16a36b5853eff84-293201892

    #Client ID
    #4708051638906536

    #Client Secret
    #WhRQP4fdTh9cLQtUbs1ljVSmj2Zz5WPz

#Credenciales de prueba

    #Public Key
    #TEST-c36a2787-71c0-4be6-9553-dc5fee95778f

    #Access token
    #TEST-4708051638906536-030215-bbf7fe073b27e6ae5c69e4b5f31a4603-293201892

import mercadopago
from mercadopago.config import RequestOptions

request_options = RequestOptions(access_token='APP_USR-4708051638906536-030215-5b711cad32b12099b16a36b5853eff84-293201892')
sdk = mercadopago.SDK("APP_USR-4708051638906536-030215-5b711cad32b12099b16a36b5853eff84-293201892")

result = sdk.payment().create(payment_data, request_options)
payment = result["response"]






#Hacer una peticion con las siguientes condiciones. Filtrado por tienda y que sea mercadoagg y solicitar todos las ordenes de compra y llevaras en formtato json para que luego
#podamos concatenar con cada code numero de pago y ver realmente cuanto costo.