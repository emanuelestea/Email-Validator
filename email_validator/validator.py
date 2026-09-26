import re
import ipaddress


EMAIL_MAX_LENGTH = 254
LOCAL_PART_MAX_LENGTH = 64
DOMAIN_MAX_LENGTH = 253


def validate_email(email: str) -> tuple[bool, str]:
    """
    Valida sintatticamente un indirizzo email.

    Returns:
        (True, "OK") se valido
        (False, "motivo") se non valido

    Nota:
        Questa funzione NON verifica che il dominio esista,
        che abbia record MX o che la casella email esista realmente.
    """

    # ---------------------------------------------------------
    # 1. Tipo e valore
    # ---------------------------------------------------------
    if not isinstance(email, str):
        return False, "L'indirizzo deve essere una stringa"

    if not email:
        return False, "Indirizzo vuoto"

    # Non consideriamo spazi esterni come parte dell'email.
    # Meglio rifiutarli anziché correggere silenziosamente l'input.
    if email != email.strip():
        return False, "L'indirizzo contiene spazi iniziali o finali"

    # ---------------------------------------------------------
    # 2. Lunghezza complessiva
    # ---------------------------------------------------------
    if len(email.encode("utf-8")) > EMAIL_MAX_LENGTH:
        return False, "Indirizzo troppo lungo"

    # ---------------------------------------------------------
    # 3. Esattamente una @
    # ---------------------------------------------------------
    if email.count("@") != 1:
        return False, "L'indirizzo deve contenere una sola @"

    local, domain = email.rsplit("@", 1)

    # ---------------------------------------------------------
    # 4. Local part
    # ---------------------------------------------------------
    if not local:
        return False, "La parte locale è vuota"

    if len(local.encode("utf-8")) > LOCAL_PART_MAX_LENGTH:
        return False, "La parte locale supera i 64 byte"

    # Spazi e caratteri di controllo
    if any(ord(c) < 32 or ord(c) == 127 for c in local):
        return False, "La parte locale contiene caratteri di controllo"

    if any(c.isspace() for c in local):
        return False, "La parte locale contiene spazi"

    # ---------------------------------------------------------
    # 5. Local part non quotata
    #
    # Supportiamo il formato comune:
    #   nome.cognome
    #   mario_rossi
    #   mario+tag
    #
    # Non supportiamo volutamente tutte le forme RFC 5322
    # più esotiche (commenti, quoted strings, ecc.).
    # ---------------------------------------------------------
    if local.startswith(".") or local.endswith("."):
        return False, "La parte locale non può iniziare o finire con '.'"

    if ".." in local:
        return False, "La parte locale non può contenere '..'"

    # Dot-atom ASCII comunemente utilizzato
    allowed_local = re.compile(
        r"^[A-Za-z0-9!#$%&'*+/=?^_`{|}~.-]+$"
    )

    if not allowed_local.fullmatch(local):
        return False, "La parte locale contiene caratteri non validi"

    # ---------------------------------------------------------
    # 6. Dominio
    # ---------------------------------------------------------
    if not domain:
        return False, "Il dominio è vuoto"

    if len(domain.encode("utf-8")) > DOMAIN_MAX_LENGTH:
        return False, "Il dominio supera i 253 byte"

    # Il dominio non può contenere spazi
    if any(c.isspace() for c in domain):
        return False, "Il dominio contiene spazi"

    # ---------------------------------------------------------
    # 7. Caso dominio letterale IPv4/IPv6
    #
    # Esempi:
    #   user@[192.168.1.1]
    #   user@[IPv6:2001:db8::1]
    #
    # Se vuoi supportarli, li gestiamo esplicitamente.
    # ---------------------------------------------------------
    if domain.startswith("[") and domain.endswith("]"):
        literal = domain[1:-1]

        if literal.lower().startswith("ipv6:"):
            literal = literal[5:]

        try:
            ipaddress.ip_address(literal)
            return True, "OK"
        except ValueError:
            return False, "Indirizzo IP nel dominio non valido"

    # ---------------------------------------------------------
    # 8. Caratteri validi nel dominio
    # ---------------------------------------------------------
    if not re.fullmatch(r"[A-Za-z0-9.-]+", domain):
        return False, "Il dominio contiene caratteri non validi"

    # ---------------------------------------------------------
    # 9. Punti del dominio
    # ---------------------------------------------------------
    if domain.startswith(".") or domain.endswith("."):
        return False, "Il dominio non può iniziare o finire con '.'"

    if ".." in domain:
        return False, "Il dominio non può contenere '..'"

    # ---------------------------------------------------------
    # 10. Label DNS
    # ---------------------------------------------------------
    labels = domain.split(".")

    for label in labels:
        if not label:
            return False, "Il dominio contiene una label vuota"

        # Una label DNS può avere al massimo 63 caratteri
        if len(label.encode("utf-8")) > 63:
            return False, f"La label '{label}' supera i 63 byte"

        # Una label non può iniziare o finire con '-'
        if label.startswith("-") or label.endswith("-"):
            return False, (
                f"La label '{label}' non può iniziare "
                "o terminare con '-'"
            )

    # ---------------------------------------------------------
    # 11. TLD
    # ---------------------------------------------------------
    # Richiediamo almeno una label finale di almeno 2 caratteri.
    #
    # Nota: questo è un controllo pratico, non una verifica
    # dell'esistenza effettiva del TLD.
    tld = labels[-1]

    if len(tld) < 2:
        return False, "Il TLD deve avere almeno 2 caratteri"

    if not re.fullmatch(r"[A-Za-z0-9]+", tld):
        return False, "Il TLD contiene caratteri non validi"

    return True, "OK"
