
class Entity(object):
    def set_attr(self, name, value):
        setattr(self, name, value)

    def set_attrs(self, dict):
        for k in dict.keys():
            setattr(self, k, dict[k])

    def to_dict(cls):
        return cls.__dict__

    def from_dict(cls, dict):
        cls.__dict__.update(dict)
        return cls


class DTE(Entity):
    name = ''
    issuer_rut = ''

    # Nombre/Razon emisor
    issuer_name = ''

    # TipoDTE
    doc_type = ''

    # Folio
    folio = ''

    # Fecha emisiom
    emission_date = ''

    # Fecha expiracion
    expiration_date = ''

    # Monto total
    total_amount = ''

    # RUT receptor
    receiver_rut = ''

    # Nombre/Razon receptor
    receiver_name = ''

    # Xml del documento
    xml = ''

    # PDF en base64
    pdf = ''

    def __init__(self):
        pass


def Enterprise(Entity):
    rut = ''
    dv = ''
    razon_social = ''
    tramoventas = ''
    num_trabajadores = ''
    rubro = ''
    subrubro = ''
    actividadeconomica = ''
    calle = ''
    numero = ''
    bloque = ''
    depto = ''
    villa = ''
    comuna = ''
    region = ''
    fecha_inicio = ''
    fecha_termino_giro = ''
    tipotermino_giro = ''
    tipo_contribuyente = ''
    subtipo_contribuyente = ''
