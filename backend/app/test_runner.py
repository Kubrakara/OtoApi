import tempfile
import subprocess

def run_schemathesis_test(swagger_json: bytes) -> dict:
    try:
        # Swagger JSON içeriğini geçici dosyaya yaz
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json", mode="w") as tmp_file:
            tmp_file.write(swagger_json.decode("utf-8"))
            tmp_file_path = tmp_file.name

        # Testi çalıştır
        result = subprocess.run(
            [
                "schemathesis",
                "run",
                tmp_file_path,
                "--base-url=http://host.docker.internal:8000",  #Buraya dikkat host.docker.internal → Docker içinden senin ana makinene ulaşır.
                "--hypothesis-seed=1",
                "--hypothesis-max-examples=5",
                "--report"
            ],
            capture_output=True,
            text=True
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr if result.returncode != 0 else None
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }