import importlib.util
import os

print("--- Checking unidic installation ---")

# Check if unidic module can be imported
unidic_spec = importlib.util.find_spec("unidic")
if unidic_spec is None:
    print("Error: 'unidic' module not found. It might not be installed.")
    exit()
else:
    print("'unidic' module is found.")

try:
    import unidic # Try to import
    print(f"Successfully imported 'unidic'. Version: {getattr(unidic, '__version__', 'N/A')}")

    dicdir_path = getattr(unidic, 'DICDIR', None)
    if dicdir_path:
        print(f"unidic.DICDIR: {dicdir_path}")

        mecabrc_path = os.path.join(dicdir_path, 'mecabrc')
        print(f"Expected mecabrc path: {mecabrc_path}")

        if os.path.exists(dicdir_path):
            print(f"Directory {dicdir_path} EXISTS.")
            if os.path.exists(mecabrc_path):
                print("SUCCESS: mecabrc file FOUND.")
                print(f"  File size: {os.path.getsize(mecabrc_path)} bytes")
            else:
                print("ERROR: mecabrc file NOT FOUND in unidic.DICDIR.")

            print(f"\n--- Contents of {dicdir_path} ---")
            try:
                for item_count, item_name in enumerate(os.listdir(dicdir_path)):
                    print(f"  {item_name}")
                    if item_count > 20: # Limit output for brevity
                        print("  ... (and possibly more)")
                        break
                if not os.listdir(dicdir_path):
                    print("  (Directory is empty or inaccessible)")
            except FileNotFoundError:
                print(f"ERROR: Could not list contents of {dicdir_path}, directory itself not found.")
            except Exception as e_ls:
                print(f"ERROR listing directory contents: {e_ls}")
        else:
            print(f"ERROR: The directory specified by unidic.DICDIR ({dicdir_path}) does NOT exist.")

    else:
        print("ERROR: 'unidic.DICDIR' attribute not found. Unidic might be improperly installed.")

except ImportError:
    print("Error: Failed to import 'unidic' even after spec was found. Installation might be corrupted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\n--- Checking fugashi installation ---")
fugashi_spec = importlib.util.find_spec("fugashi")
if fugashi_spec is None:
    print("Error: 'fugashi' module not found.")
else:
    print("'fugashi' module is found.")
    try:
        import fugashi
        print(f"Successfully imported 'fugashi'. Version: {getattr(fugashi, '__version__', 'N/A')}")
    except ImportError:
        print("Error: Failed to import 'fugashi'.")
    except Exception as e_f:
        print(f"An unexpected error occurred with fugashi: {e_f}")