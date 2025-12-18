from cryptography.hazmat.primitives.serialization import load_pem_public_key

with open("student_public.pem", "rb") as f:
    load_pem_public_key(f.read())

print("PUBLIC KEY IS VALID")
