---
source_url: https://ai.google.dev/gemini-api/docs/billing?hl=es-419
fetched_at: 2026-07-27T04:41:52.334703+00:00
title: "Facturaci\u00f3n \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Facturación

En esta guía, se proporciona una descripción general de las diferentes opciones de facturación de la API de Gemini, se explica cómo habilitar la facturación y supervisar el uso, y se responden las preguntas frecuentes sobre la facturación.

## Acerca de la facturación y los niveles

La facturación de la API de Gemini se basa en tu historial de pagos.

| Nivel de uso | Calificación | [Límite del nivel de facturación](#spend-caps) |
| --- | --- | --- |
| **Gratis** | [Proyecto activo](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419#google-cloud-projects) o prueba gratuita | N/A |
| **Nivel 1** | [Configura y vincula una cuenta de facturación activa](#setup-billing) | $250 |
| **Nivel 2** | Se pagaron USD 100 y pasaron 3 días desde el primer pago exitoso. | $2,000 |
| **Nivel 3** | Se pagaron USD 1,000 y pasaron 30 días desde el primer pago exitoso. | USD 20,000 a más de USD 100,000 |

Las cuentas nuevas comienzan con el nivel gratuito, que permite el acceso a [ciertos modelos](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419) en la API de Gemini y AI Studio, hasta los [límites de frecuencia](https://aistudio.google.com/rate-limit?hl=es-419) del nivel gratuito de los modelos.

Para implementar tus aplicaciones directamente desde el modo de compilación, puedes usar el **nivel básico de Google Cloud**. Este nivel te permite publicar hasta 2 aplicaciones de pila completa sin configurar un proyecto de Google Cloud ni una cuenta de facturación.
Consulta [Cómo realizar la implementación desde Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=es-419) para obtener más detalles y consulta la [documentación del nivel básico de Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=es-419) para obtener más información.

Para acceder a límites de frecuencia más altos, usar modelos avanzados y garantizar que tus instrucciones y respuestas **no** se usen para mejorar los productos de Google\*, puedes [vincular una cuenta de facturación](#setup-billing) y [pagar por adelantado](#prepay) para cambiar a los niveles pagados.
Luego, avanzarás a niveles superiores según la inversión acumulada y la antigüedad de la cuenta. En el nivel 3, es posible que tengas la opción de cambiar a la facturación [pospago](#postpay).

Los niveles, los límites de frecuencia y los límites de las cuentas de facturación se determinan a nivel de la [cuenta de facturación](#cloud-billing).

\* *Privacidad de datos de nivel empresarial: Para obtener más información sobre el uso de datos para los servicios pagados, consulta las [Condiciones del Servicio](https://ai.google.dev/gemini-api/terms?hl=es-419#data-use-paid).*

## Configura la facturación para acceder al nivel pagado

Puedes crear un proyecto y configurar la facturación, o importar un proyecto existente, para actualizarte al nivel pagado en [Google AI Studio](https://aistudio.google.com/projects?hl=es-419).
Actualizar del nivel gratuito al nivel pagado implica vincular una cuenta de facturación y [pagar por adelantado](#prepay) para agregar un mínimo de USD 10 (o el equivalente en otras monedas) de créditos a tu cuenta.

1. Ve a la página [Claves de API](https://aistudio.google.com/api-keys?hl=es-419) o [Proyectos](https://aistudio.google.com/projects?hl=es-419) de AI Studio, o a cualquier lugar en el que veas el botón **Configurar facturación** en AI Studio.
   - De forma predeterminada, los usuarios nuevos tendrán un [proyecto y una clave de API](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419#google-cloud-projects) creados para ellos.
   - Si necesitas una clave nueva, haz clic en [**Crear clave de API**](https://aistudio.google.com/api-keys?hl=es-419) y sigue las instrucciones del diálogo para agregar un par clave-proyecto a la tabla.
2. Busca el proyecto del nivel gratuito que deseas actualizar al nivel pagado y haz clic en **Configurar facturación** en la columna *Nivel de facturación*.
3. Si nunca configuraste una cuenta de facturación de Google, haz lo siguiente:
   - Se te pedirá que selecciones tu país para aceptar las Condiciones del Servicio.
   - Luego, completa o confirma tu información de contacto y forma de pago para continuar.
4. Si ya configuraste cuentas de facturación de Google en el pasado, haz lo siguiente:
   - Se te pedirá que elijas entre tus cuentas de facturación existentes.
   - Si no quieres usar ninguna de tus cuentas existentes, haz clic en **Agregar una nueva cuenta de facturación** y completa o confirma tu información de contacto y forma de pago para continuar.
5. A continuación, sucederá una de las siguientes situaciones:
   - Se te solicitó que prepagues un mínimo de USD 10 para completar la configuración de facturación (lo que significa que tu cuenta se asignó automáticamente al plan de facturación de [prepago](#prepay)).
   - Se te ofrece la opción de elegir entre los planes de facturación [Prepago](#prepay) y [Pospago](#postpay) para tu cuenta.
   - Se asignará a un plan de facturación [pospago](#postpay) durante un período intermedio hasta que el nuevo sistema de prepago se propague a todos los usuarios (a partir del 23 de marzo de 2026).
6. Después de realizar el prepago o seleccionar la opción de pospago, se completará la configuración de tu cuenta.

### Actualiza al siguiente nivel pagado

Si ya estás en un nivel pagado y cumples con los [criterios](#about-billing) para cambiar de plan, se actualizará automáticamente al siguiente nivel (sujeto a los [tiempos de procesamiento](#processing-times)).

## Verifica el estado de la facturación

Después de [vincular una cuenta de facturación](#setup-billing) a tu proyecto, puedes supervisar su estado en la [página Facturación de AI Studio](https://aistudio.google.com/billing?hl=es-419). A diferencia del nivel gratuito, el estado del nivel pagado es dinámico. Si bien tu nivel de uso se determina según el historial de tu cuenta, la API de Gemini solo atenderá solicitudes si tienes un saldo de crédito [prepago](#prepay) positivo.

En la página [Proyectos](https://aistudio.google.com/projects?hl=es-419), podrás ver el nivel y el plan de facturación de tu proyecto en la columna *Nivel de facturación*. En las columnas *Nivel de facturación* o *Estado*, se muestran las acciones de estado de facturación que tal vez debas realizar para un proyecto:

- “***Configurar la facturación***” si el proyecto no tiene una cuenta de facturación adjunta
- "***Configurar prepago***" si el proyecto tiene una cuenta de facturación adjunta, pero debe usar un plan de facturación de [prepago](#prepay) que debe configurarse
- "***Sin créditos***" si se requiere una cuenta de facturación para comprar créditos, pero no se configuró la cuenta de pagos de prepago o se agotó el saldo de crédito disponible.

Haz clic en cualquiera de los mensajes para continuar con las acciones necesarias.

## Supervisa el uso

Puedes supervisar el uso de la API de Gemini en [Google AI Studio](https://aistudio.google.com/usage?hl=es-419) en **Panel** > **Uso**.

## Planes de facturación

Los planes de facturación de la API de Gemini y AI Studio se dividen en dos categorías que determinan cuándo pagas por el uso: prepago y pospago. Puedes consultar el plan de facturación asignado y administrar las formas de pago en la página [Facturación de AI Studio](https://aistudio.google.com/billing?hl=es-419).

### Prepago

En el plan de facturación prepagado, compras créditos para tu saldo prepagado antes de usar la API de Gemini, y los costos de uso de la API se deducen de tu saldo de crédito prepagado [casi en tiempo real](#processing-times).
Puedes realizar el pago por adelantado [agregando créditos](#buy-credits) a tu cuenta o configurando la [recarga automática](#auto-reload). Después de comprar créditos, los que no se usen vencerán después de 12 meses y [no serán reembolsables](#refunds), excepto después de [cambiar a una cuenta de pospago](#postpay).

Cuando el saldo de crédito de prepago de la cuenta de facturación llegue a USD 0, todas las claves de API de todos los proyectos vinculados a esa cuenta de facturación dejarán de funcionar simultáneamente.
Los créditos prepagados solo se aplican a los costos de uso de la API de Gemini. No puedes usarlos para pagar otros servicios de Google Cloud.

Los usuarios nuevos tienen el plan de facturación de prepago de forma predeterminada. Es posible que los proyectos anteriores a la introducción de los planes de facturación de prepago y pospago deban [actualizar los detalles de facturación del proyecto](#verify-billing) antes de seguir usando la API de Gemini.

*Ten en cuenta que el prepago no está disponible para las cuentas [facturadas (o sin conexión)](https://docs.cloud.google.com/billing/docs/concepts?hl=es-419#billing_account_types).*

#### Compre créditos

Puedes comprar créditos manualmente antes de usar la API de Gemini para cargarlos en el saldo de crédito de tu cuenta prepagada.

Para comprar créditos, ve a la página [Facturación de AI Studio](https://aistudio.google.com/billing?hl=es-419) y selecciona **Comprar créditos**.
La compra mínima es de USD 10. El importe máximo de créditos que puedes pagar por adelantado es de USD 5,000.

#### Volver a cargar automáticamente

La recarga automática es una función opcional que recarga automáticamente tu saldo de crédito prepagado cuando se está agotando. Esto es útil para evitar interrupciones del servicio.

Puedes configurar la recarga automática y ver su estado en la tarjeta *Créditos disponibles* de la página [Facturación de AI Studio](https://aistudio.google.com/billing?hl=es-419). Haz clic en **Configurar la recarga automática** o **Administrar la recarga automática** para establecer tu forma de pago, el importe de la recarga y el saldo mínimo que activa un pago de recarga.

#### Límite de carga automática mensual

El límite de carga automática mensual está disponible para los usuarios de prepago y ayuda a evitar costos inesperados por las recargas automáticas frecuentes de crédito.
Usa esta función para establecer un límite máximo para las recargas automáticas de crédito en un solo ciclo de facturación. Una vez que el importe total de las recargas automáticas en un ciclo de facturación alcanza este límite, el sistema inhabilita la recarga automática hasta el comienzo del mes siguiente. Los pagos únicos que inicias de forma manual no se descuentan de este límite.

Para establecer el límite de pago automático mensual cuando la recarga automática está habilitada, sigue estos pasos:

1. Ve a la página [Facturación de AI Studio](https://aistudio.google.com/billing?hl=es-419).
2. Haz clic en **Administrar la recarga automática**.
3. Expande la sección **Límite mensual** y, luego, ingresa el límite mensual máximo para las recargas automáticas.
4. Haz clic en **Guardar**.

### Pospago

En el plan de facturación pospago, tu cuenta de facturación de Cloud acumula costos y se te cobra automáticamente al final del mes o cuando tus costos alcanzan un [límite de inversión asignado automáticamente](#tier-spend-caps) según el nivel de tu cuenta.
El pago se cobra a la forma de pago asociada a tu cuenta de pagos pospago, que puedes administrar en la página [Facturación de AI Studio](https://aistudio.google.com/billing?hl=es-419).

Cuando cumples con los [criterios del nivel 3](#about-billing), puedes cambiar manualmente del plan prepagado al pospagado. Para cambiar de plan, deberás hacer clic en el botón **Cambiar a pospago** que aparece en la esquina superior derecha de la página [Facturación de AI Studio](https://aistudio.google.com/billing?hl=es-419) cuando tu cuenta cumpla con los requisitos.

Luego, en la página **Facturación**, podrás ver tu saldo, las fechas de vencimiento y los pagos anteriores, así como realizar pagos y administrar las formas de pago.

Cuando [configures la facturación](#setup-billing) para un proyecto nuevo, si cumples con los requisitos para el pospago, tendrás la opción de elegir entre prepago y pospago en el diálogo de [configuración de facturación](#setup-billing).

Después de cambiar una cuenta de facturación de Cloud para que use el plan de facturación con posterioridad al pago, todos los proyectos vinculados a esa cuenta de facturación se cambiarán al plan con posterioridad al pago. No puedes volver a cambiar esa cuenta de facturación al plan de facturación de prepago. Puedes trasladar un proyecto a una cuenta de facturación con un plan de facturación diferente para cambiar el ciclo de facturación de ese proyecto. Visita la documentación de Cloud sobre la [administración de la facturación de proyectos](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=es-419).

Puedes obtener más información sobre el ciclo de cobro de Postpago en la [guía de Facturación de Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=es-419).

## Límites de inversión

La API de Gemini admite límites de inversión mensuales a nivel de la cuenta de facturación y del proyecto. Estos controles están diseñados para proteger tu cuenta de cargos inesperados y el ecosistema para garantizar la disponibilidad del servicio.

*Ten en cuenta que los límites de inversión no están disponibles para las cuentas [facturadas (o sin conexión)](https://docs.cloud.google.com/billing/docs/concepts?hl=es-419#billing_account_types).*

### Límites de inversión del proyecto

Puedes establecer tus propios límites de inversión a [nivel del proyecto](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419#google-cloud-projects) en AI Studio.
Esto es útil si tienes varios proyectos en la misma cuenta de facturación y deseas asegurarte de que cada uno tenga acceso a una cantidad suficiente del límite de gasto acumulativo.

Las cuentas con los [roles](https://docs.cloud.google.com/iam/docs/roles-overview?hl=es-419) de editor, propietario o administrador del proyecto pueden establecer límites de inversión por proyecto en AI Studio en la página [Inversión](https://aistudio.google.com/spend?hl=es-419) en **Límite de inversión mensual** > **Editar límite de inversión**.

Para obtener detalles sobre los permisos específicos de IAM de Google Cloud necesarios para ver o editar los límites de inversión y la información de facturación en AI Studio, consulta la [guía de solución de problemas de AI Studio](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=es-419#iam-permissions).

Si [trasladas un proyecto a una cuenta de facturación diferente](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=es-419#change_the_billing_account_for_a_project), se mantendrá cualquier límite de inversión que ya hayas establecido para ese proyecto, pero la inversión acumulada se restablecerá a USD 0 para el nuevo ciclo de facturación.

Las tareas de larga duración, como las finalizaciones en [modo por lotes](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419) y las sesiones de agentes, pueden generar cargos por excedentes que superen el límite de inversión de tu proyecto.

Los tiempos de procesamiento de los datos de facturación pueden retrasarse en AI Studio hasta alrededor de 10 minutos. Es posible que experimentes excedentes más allá del límite de tu proyecto si los datos de facturación no se procesan antes de que se acumulen más cargos.

### Límites de inversión de los niveles de la cuenta de facturación

Cada [nivel](#about-billing) tiene un límite de inversión mensual máximo:

| Nivel de uso | Límite de inversión |
| --- | --- |
| **Gratis** | N/A |
| **Nivel 1** | $250 |
| **Nivel 2** | $2,000 |
| **Nivel 3** | USD 20,000 a USD 100,000 |

Se aplican límites de uso mensuales para la API de Gemini a nivel de la [cuenta de facturación](#cloud-billing). Si bien los límites predeterminados están preestablecidos, puedes [solicitar un aumento](https://docs.google.com/forms/d/e/1FAIpQLSdiP6BWJyNNN65lnwnlOr-5Kv0MOFp0jLQyqi_ixVCfddqWBw/viewform?hl=es-419) para admitir un mayor uso. La inversión total se agrega en todos los proyectos vinculados que tienen habilitado el servicio de la API de Gemini. Después de que el total acumulado de la cuenta alcance el límite del nivel, se pausará el servicio para todos los proyectos vinculados a esa cuenta de facturación hasta el inicio del próximo ciclo de facturación (el 1 de cada mes).

#### Evalúa la inversión de tu cuenta de facturación

Para evaluar tu inversión mensual histórica y determinar si los nuevos [límites de inversión de nivel de la cuenta de facturación](#tier-spend-caps) afectarán tus proyectos en curso, sigue estos pasos:

1. En la consola de Google Cloud, consulta la página [Informes de tu cuenta de Facturación de Cloud](https://console.cloud.google.com/billing/reports?hl=es-419).
   - Si tienes más de una cuenta de facturación, en el mensaje, elige la cuenta de Facturación de Cloud de la que quieres ver informes de costos.
2. De forma predeterminada, el informe se establece en "Agrupar por servicio" en el "Mes actual". Verás **API de Gemini** en la columna **Servicio** y la inversión total en la columna **Costo de uso** de la tabla.
3. Para ver los costos detallados limitados al uso de la API de Gemini, configura el filtro **Agrupar por** para agrupar por **SKU** y el filtro **Servicios** en **API de Gemini**.
4. Ajusta el filtro **Período por fecha de uso** al período que desees para evaluar tu inversión histórica en un período.

## Tiempos de procesamiento

Los indicadores y las actualizaciones de facturación no siempre se realizan en tiempo real.

- **Uso de créditos**: Por lo general, los costos de uso se deducen de tu saldo en cuestión de minutos.
- **Confirmación del pago**: Si bien la mayoría de los pagos con tarjeta son instantáneos, algunas formas de pago (como las transferencias bancarias) pueden tardar varios días en procesarse. Los servicios solo se reanudan o actualizan después de que se confirma oficialmente la compra de créditos.
- **Actualizaciones de nivel**: Después de un pago exitoso o cuando cumples con los [criterios de actualización](#about-billing), las actualizaciones de nivel suelen reflejarse en un plazo de 10 minutos.
- **Gráficos de desglose del costo total**: Los gráficos que muestran el desglose del costo total en las páginas [Facturación](https://aistudio.google.com/billing?hl=es-419) y [Inversión](https://aistudio.google.com/spend?hl=es-419) pueden tardar hasta 24 horas en actualizarse.

Lee las guías de Facturación de Cloud sobre el [ciclo de facturación](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=es-419#delayed-billing) y las latencias de [transacciones](https://docs.cloud.google.com/billing/docs/how-to/view-history?hl=es-419#missing-transactions) para obtener más información sobre posibles retrasos en la facturación.

## Reembolsos

No se permiten reembolsos para las cuentas de facturación **prepago**, excepto cuando se cambian los tipos de cuenta.

**Cuando una cuenta prepagada cambia al tipo de cuenta pospagada** (después de que cumples con los [criterios](#about-billing) y [actualizas manualmente](#postpay) tu cuenta), se cierra la cuenta prepagada y los créditos prepagados restantes se reembolsan automáticamente a la forma de pago registrada.

Si [cierras](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=es-419#close-a-billing-account) tu cuenta prepagada por cualquier motivo que no sea la actualización a una cuenta pospagada, se perderán los créditos prepagados restantes.

Los créditos comprados vencen después de 1 año. Después del vencimiento, los créditos se pierden y no se pueden recuperar.

Las cuentas de **pospago** cumplen con la [política de reembolsos de Google Cloud](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=es-419#request_a_refund).

## Cuentas de facturación de Cloud

La API de Gemini usa [cuentas de facturación de Cloud](https://cloud.google.com/billing/docs/concepts?hl=es-419) para los servicios de facturación, que puedes [configurar directamente en AI Studio](#setup-billing).
Puedes usar AI Studio para hacer un seguimiento de los gastos, comprender los costos y realizar pagos.

Los niveles, los límites de frecuencia y los límites de las cuentas de facturación se determinan a nivel de la cuenta de facturación.

### Proyectos y claves de API

Todos los [proyectos](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419#google-cloud-projects) vinculados a una cuenta de Facturación de Cloud heredan el nivel de uso y los límites de tarifas y los límites de cuenta asociados de la cuenta de facturación. Si [cambias un proyecto](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=es-419#change_the_billing_account_for_a_project) de una cuenta de facturación a otra, su nivel y, posteriormente, los límites de frecuencia y los límites de la cuenta cambiarán al nivel de la nueva cuenta de facturación.

El gasto acumulado (en todos los productos de Google Cloud) y la antigüedad de la cuenta en todos los proyectos vinculados a una cuenta de facturación se tienen en cuenta para las [calificaciones de nivel](#about-billing) de esa cuenta de facturación.

Puedes [desvincular un proyecto](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=es-419#disable_billing_for_a_project) de su cuenta de facturación para volver al nivel gratuito.

Las [claves de API](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419) son credenciales que se generan dentro de un proyecto.
No tienen parámetros de configuración de facturación independientes, sino que heredan los límites de nivel y el estado de facturación del proyecto. El uso acumulativo de todas las claves de un proyecto se incluye en el límite de inversión de ese proyecto y en la inversión total de la cuenta de facturación.

## Preguntas frecuentes

En las siguientes secciones, se proporcionan respuestas a las preguntas frecuentes.

### ¿Qué me cobran?

Los precios de la API de Gemini se basan en lo siguiente:

- La cantidad de tokens de entrada
- La cantidad de tokens de salida
- La cantidad de tokens almacenados en caché
- La duración del almacenamiento de los tokens en caché

Para obtener información sobre los precios, consulta la [página de precios](https://ai.google.dev/pricing?hl=es-419).

### ¿Dónde puedo ver mi cuota?

Puedes ver tus límites de cuota y del sistema en [AI Studio](https://aistudio.google.com/usage?hl=es-419).

### ¿Cómo puedo cambiar a un nivel de límite de frecuencia más alto o solicitar más cuota?

Se te otorgará automáticamente más cuota cuando tu cuenta alcance los próximos [requisitos de nivel](https://ai.google.dev/gemini-api/docs/rate-limits?hl=es-419#usage-tiers).

### ¿Puedo usar la API de Gemini de forma gratuita en el EEE (incluida la UE), el Reino Unido y Suiza?

Sí, ofrecemos el nivel gratuito y el nivel pagado en [muchas regiones](https://ai.google.dev/gemini-api/docs/available-regions?hl=es-419).

### Si configuro la facturación con la API de Gemini, ¿se me cobrará por mi uso de Google AI Studio?

El uso de AI Studio sigue siendo gratuito, a menos que los usuarios vinculen una clave de API pagada para acceder a las funciones pagadas.
Una vez que vincules una clave de API pagada como parte de un proyecto pagado en AI Studio, se te cobrará el uso de AI Studio para esa clave. Puedes cambiar entre proyectos del nivel pagado y proyectos del nivel gratuito según sea necesario con las claves de API respectivas vinculadas a cada tipo.

### Si estoy en el nivel gratuito, ¿cómo actualizo a niveles superiores?

Para acceder a niveles más altos, debes configurar la facturación en tu proyecto. Haz clic en [**Configurar facturación**](#setup-billing) en Google AI Studio. En este proceso, se te guiará para que selecciones o crees una cuenta de Facturación de Cloud. Si debes usar el modelo de facturación prepagada, el proceso de **configuración de la facturación** te guiará para crear tu cuenta prepagada vinculada a tu cuenta de Facturación de Cloud.

### ¿Puedo usar 1 millón de tokens en el nivel gratuito?

El nivel gratuito de la API de Gemini varía según el modelo seleccionado. Por el momento, puedes probar la ventana de contexto de 1 millón de tokens de las siguientes maneras:

- En Google AI Studio
- Con planes sin cargo para modelos seleccionados
- Con planes pospago

### ¿Puedo volver al nivel gratuito después de actualizar a niveles superiores (pagados)?

Para cambiar a la capa gratuita, puedes [inhabilitar la facturación](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=es-419#disable_billing_for_a_project) en cada uno de los proyectos a los que quieras cambiar.

### ¿Cómo puedo calcular la cantidad de tokens que uso?

Usa el método [`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=es-419#count_tokens) para contar la cantidad de tokens. Consulta la [guía de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) para obtener más información sobre ellos.

### Si me registro para obtener mi primera cuenta de Facturación de Cloud a través de AI Studio, ¿seguiré obteniendo una prueba gratuita de Google Cloud?

Cuando te registras para obtener tu primera cuenta de Facturación de Cloud, comienza tu [prueba gratuita de Google Cloud](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=es-419#free-trial) y se te otorga un [crédito de bienvenida](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=es-419#welcome-credits) de USD 300.
Sin embargo, esos créditos no se pueden usar para pagar el uso de AI Studio. Puedes usar el crédito de bienvenida para pagar otros servicios aptos dentro de Google Cloud (ten en cuenta que, una vez que se consuman o venzan esos créditos (en un plazo de 90 días), los costos de uso adicionales se facturarán automáticamente a tu forma de pago establecida).

### ¿Puedo usar mi crédito de bienvenida de Google Cloud con la API de Gemini?

No, el [crédito de bienvenida](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=es-419#welcome-credits) o el crédito de prueba gratuita de Google Cloud no se pueden usar para la API de Gemini ni AI Studio.

Si se te otorgó un crédito de bienvenida de Google Cloud antes de que los productos dejaran de ser aptos, puedes usar los créditos restantes en la API de Gemini y AI Studio hasta que venzan (después de 90 días).

### ¿La prueba gratuita de Google Cloud se aplica al uso de la API de Gemini?

No. A partir de marzo de 2026, los costos de uso de la API de Gemini se excluyen específicamente del programa de [prueba gratuita de Google Cloud de USD 300](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=es-419#free-trial).

### ¿Cómo funcionan los créditos de Google Cloud con la opción de prepago?

Los usuarios prepagados primero deben [comprar créditos prepagados](#buy-credits) antes de que se puedan aplicar créditos de Google Cloud aptos al uso de la API de Gemini. Una vez que tengas un saldo de crédito prepagado activo, los créditos de Google Cloud aptos para la API de Gemini se consumirán antes que tu saldo de crédito prepagado. Cuando el saldo de crédito de prepago de la cuenta de facturación llegue a USD 0, ya no se consumirán los créditos de Google Cloud.

No todos los créditos de Google Cloud, como el [crédito de bienvenida de Google Cloud](#cloud-credits), se pueden usar para la API de Gemini y AI Studio.

### ¿Cómo se maneja la facturación?

El sistema de [facturación de Cloud](https://cloud.google.com/billing/docs/concepts?hl=es-419) se encarga de la facturación de la API de Gemini. Obtén más información sobre la configuración de la Facturación de Cloud en el producto en la [documentación de la Facturación de Cloud](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=es-419).

### ¿Se me cobra por las solicitudes con errores?

Si tu solicitud falla con un error 400 o 500, no se te cobrarán los tokens que se usaron. Sin embargo, la solicitud se seguirá contando en tu cuota.

### ¿Se factura `GetTokens`?

Las solicitudes a la API de `GetTokens` no se facturan y no se descuentan de la cuota de inferencia.

### ¿Cómo se manejan mis datos de Google AI Studio si tengo una cuenta de API pagada?

Consulta las [Condiciones del Servicio](https://ai.google.dev/gemini-api/terms?hl=es-419#paid-services) para obtener detalles sobre cómo se manejan los datos cuando se habilita la facturación de Cloud (consulta "Cómo Google Usa sus Datos" en "Servicios Pagados"). Ten en cuenta que tus instrucciones de Google AI Studio se tratan según las mismas condiciones de "Servicios Pagados", siempre y cuando al menos 1 proyecto de API tenga habilitada la facturación, lo que puedes validar en la [página de la clave de la API de Gemini](https://aistudio.google.com/api-keys?hl=es-419) si ves algún proyecto marcado como "Pagado" en "Plan".

### ¿Qué es la facturación prepagada y quiénes deben usar el modelo de facturación prepagada?

La facturación prepagada permite a los usuarios de la API de Gemini en AI Studio comprar créditos por adelantado.
A partir del 23 de marzo de 2026, es posible que los usuarios nuevos de AI Studio deban tener el plan de facturación prepago. Durante el proceso de [configuración de la facturación](#setup-billing) de AI Studio, la IU te guiará por el flujo de configuración de la facturación y te indicará si debes realizar un pago por adelantado.

### ¿Cómo compro créditos de prepago? ¿Hay un importe mínimo o máximo?

Puedes [comprar créditos](#buy-credits) en la página de facturación de AI Studio. Durante el proceso de compra, la IU proporcionará el importe mínimo previo a la compra que se requiere para tu región y nivel, así como un importe máximo que puede haber en tu cuenta en un momento determinado.

### ¿Puedo configurar mi cuenta de prepago para que compre automáticamente más créditos según sea necesario?

Sí, te recomendamos que configures la [recarga automática](#auto-reload) en la configuración de facturación de AI Studio. Especificas un saldo de créditos de "activación" (p.ej., "cuando mi saldo sea inferior a USD 30") y un "valor de recarga" (p.ej., "agregar USD 100").

### ¿Puedo limitar la cantidad de cargos por recarga automática?

Sí, los usuarios de Prepay pueden establecer un [límite de carga automática mensual](#monthly-auto-charge-limit) en el widget de **Recarga automática**. Cuando el importe total de las recargas automáticas en un ciclo de facturación alcanza este límite, el sistema inhabilita la recarga automática hasta el mes siguiente. Las compras de crédito manuales no se tienen en cuenta para este límite.

### ¿Puedo obtener un reembolso por los créditos que no usé?

Todos los créditos de la API prepagada vencen después de 1 año y no se pueden reembolsar. Lee la [política de reembolsos para cuentas de prepago](#refunds).

### ¿Mis créditos de prepago vencen?

Sí, los créditos vencen 12 meses después de la fecha de compra.

### ¿Qué sucede cuando mi saldo de crédito prepagado llega a USD 0?

Todos los servicios de la API de Gemini en todos los proyectos pagados con esa cuenta prepagada de Facturación de Cloud se detendrán de inmediato para evitar que se generen más cargos. Tus proyectos no se cambian automáticamente al nivel gratuito.

Para restablecer el servicio en tu nivel de nivel pagado actual, debes [comprar créditos adicionales](#buy-credits). Después de comprar créditos, deberías poder usar la API de Gemini. Ten en cuenta que puede haber una [demora](#processing-times) mientras nuestros sistemas se actualizan para reflejar el saldo de tu crédito.

De manera opcional, para cambiar a la capa gratuita, puedes [inhabilitar la facturación](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=es-419#disable_billing_for_a_project) en los proyectos a los que deseas cambiar.

### ¿Por qué se detuvo mi uso a pesar de que mi saldo de crédito de prepago es superior a USD 0?

Es posible que hayas alcanzado el [límite de uso](#tier-spend-caps) de tu nivel actual.
Los límites de uso aumentarán automáticamente a medida que avances a niveles más altos. El uso de la API de Gemini en AI Studio también puede verse afectado por [el estado de tu cuenta de Facturación de Cloud](#missed-payment).

### ¿Por qué el saldo de crédito de mi cuenta de prepago es negativo?

Debido a la complejidad de nuestros sistemas de facturación y procesamiento, es posible que haya [demoras](#processing-times) en nuestra capacidad de cortar el uso después de que consumas todos tus créditos. Este uso adicional puede aparecer como un saldo de crédito negativo en el panel de facturación de AI Studio. Si esto sucede, se pausará el servicio y el saldo negativo se deducirá de tu próxima compra de crédito.

Para evitar que se pause tu servicio de la API de Gemini, te recomendamos que configures la [recarga automática](#auto-reload) para comprar más créditos automáticamente cuando tu saldo de créditos sea inferior a un valor que especifiques.

### ¿Puedo usar mis créditos de prepago para otros servicios de Google Cloud, como Gemini Enterprise Agent Platform?

No, los créditos prepagados están estrictamente vinculados al uso de la API de Gemini. Cualquier otro servicio de Google Cloud que uses (Compute, Storage, Gemini Enterprise Agent Platform) se factura con el [ciclo de cobro de Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=es-419) estándar.

### ¿Puedo cambiarme a un plan de facturación pospago?

Cuando establezcas un historial de pagos y [alcances un nivel apto](#about-billing) para el plan de facturación pospago, puedes optar por transferir todos tus costos futuros de uso de la API de Gemini a un [ciclo de cobro pospago](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=es-419#view-your-charging-cycle) estándar y consolidado de Google Cloud.

### ¿Qué sucede con mis créditos prepagados si me cambio a la modalidad pospago?

Cuando actualizas a [pospago](#postpay), la Facturación de Cloud cierra tu cuenta de pagos de prepago, desactiva la [recarga automática](#auto-reload) y te reembolsa automáticamente los créditos de prepago que no se usaron (sujeto al tiempo de procesamiento estándar de los reembolsos).

### ¿Dónde puedo ver mi saldo actual de crédito de prepago y mi historial de transacciones?

Toda la administración del saldo y el historial de transacciones de la API de Gemini deben realizarse directamente en la pestaña Facturación de Google AI Studio.

### ¿Por qué veo el mensaje "El tipo de cuenta de facturación está inactivo o no es compatible"?

Es posible que se bloqueen las interacciones de pagos en la [página Facturación de AI Studio](https://aistudio.google.com/billing?hl=es-419) y se reemplacen por el mensaje "El tipo de cuenta de facturación está inactivo o no se admite" si el tipo de cuenta de facturación o el estado de la cuenta de facturación que seleccionaste no son aptos para el nivel pagado de AI Studio.

Consulta la [consola de Cloud](https://console.cloud.google.com/billing/?hl=es-419) para ver el estado de tu cuenta de facturación. Un tipo no apto podría ser *Cuenta de prueba gratuita*, en cuyo caso puedes [activar la facturación](#setup-billing) en AI Studio para cumplir con los requisitos. Un estado inactivo podría ser *Cerrada*, en cuyo caso puedes [reabrir la cuenta](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=es-419).

### ¿Los costos de uso de la API de Gemini aparecerán en la consola de Google Cloud?

Sí, los costos de la API de Gemini, junto con los costos asociados a cualquier otro servicio de Google Cloud que se pague con tu cuenta de Facturación de Cloud, se pueden ver en las [páginas de administración de costos](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle?hl=es-419#cost-reports) de la [consola de Facturación de Cloud](https://console.cloud.google.com/billing?hl=es-419). Ten en cuenta que solo puedes administrar tu saldo de crédito prepagado en AI Studio.

### ¿Por qué no se muestra mi uso de la API de Gemini en la consola de Cloud Billing, cuando puedo verlo en la facturación de AI Studio, junto con el consumo de mis créditos?

Google Cloud y AI Studio informan los datos de uso a la Facturación de Cloud en intervalos variables. Debido a la complejidad de nuestros sistemas de facturación y procesamiento, es posible que haya una demora entre el uso que hagas de los servicios y la disponibilidad para ver el uso y los costos en la Facturación de Cloud. Por lo general, los detalles de tus costos están disponibles en un plazo de un día, aunque, a veces, pueden tardar más de 24 horas.
Obtén más información sobre la facturación diferida en la [documentación de Facturación de Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=es-419#delayed-billing).

### Si uso otros servicios de Google Cloud con costos sujetos a un ciclo de facturación pospago, ¿qué sucede si no realizo un pago?

Si no pagas otros servicios de Google Cloud, es posible que se suspenda tu acceso a la API de Gemini en AI Studio, **independientemente de la cantidad de créditos prepagados que tengas disponibles**. El uso de AI Studio se basa en una cuenta de facturación de Google Cloud, que puede compartir la facturación prepagada para AI Studio y la facturación pospagada para otros servicios de Cloud. Si hay un problema con tu saldo de Postpay, se detendrán todos los servicios vinculados a esa cuenta. Se suspenderá tu uso de la API de Gemini si tu cuenta de Facturación de Cloud se marca por problemas como los siguientes:

- Un saldo vencido o con morosidad
- Un pago rechazado
- Una forma de pago no válida o vencida

Para restablecer el servicio, debes [resolver el problema de la cuenta de pospago](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=es-419#resolving-declined-payments) en la consola de Facturación de Google Cloud. Una vez que resuelvas el problema, recuperarás el acceso a tus créditos y servicios prepagados de la API de Gemini.

### ¿Dónde puedo obtener ayuda con la facturación?

Para obtener ayuda con la facturación, consulta [Obtén asistencia para la facturación de Cloud](https://cloud.google.com/support/billing?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-07 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-07 (UTC)"],[],[]]
