"""
Diagnostic Script - Test All Dependencies
Run this to identify which package is causing issues
"""

import sys

print("=" * 60)
print("🔍 DEPENDENCY DIAGNOSTIC TEST")
print("=" * 60)

# Test Python version
print(f"\n✓ Python Version: {sys.version}")
print(f"✓ Python Executable: {sys.executable}")

# List of required packages
packages = [
    'flask',
    'flask_sqlalchemy',
    'flask_login',
    'flask_bcrypt',
    'qrcode',
    'PIL',
    'pandas',
    'openpyxl',
    'werkzeug'
]

print("\n" + "=" * 60)
print("📦 TESTING IMPORTS")
print("=" * 60)

failed_imports = []
successful_imports = []

for package in packages:
    try:
        if package == 'flask_sqlalchemy':
            import flask_sqlalchemy
            successful_imports.append((package, flask_sqlalchemy.__version__))
            print(f"✓ {package:20} - Version {flask_sqlalchemy.__version__}")
        elif package == 'flask_login':
            import flask_login
            successful_imports.append((package, flask_login.__version__))
            print(f"✓ {package:20} - Version {flask_login.__version__}")
        elif package == 'flask_bcrypt':
            import flask_bcrypt
            successful_imports.append((package, flask_bcrypt.__version__))
            print(f"✓ {package:20} - Version {flask_bcrypt.__version__}")
        elif package == 'flask':
            import flask
            successful_imports.append((package, flask.__version__))
            print(f"✓ {package:20} - Version {flask.__version__}")
        elif package == 'qrcode':
            import qrcode
            successful_imports.append((package, qrcode.__version__))
            print(f"✓ {package:20} - Version {qrcode.__version__}")
            # Test QRCode class specifically
            try:
                qr = qrcode.QRCode()
                print(f"  ✓ qrcode.QRCode() works!")
            except Exception as e:
                print(f"  ✗ qrcode.QRCode() FAILED: {e}")
                failed_imports.append((package, str(e)))
        elif package == 'PIL':
            from PIL import Image
            import PIL
            successful_imports.append((package, PIL.__version__))
            print(f"✓ {package:20} - Version {PIL.__version__}")
        elif package == 'pandas':
            import pandas
            successful_imports.append((package, pandas.__version__))
            print(f"✓ {package:20} - Version {pandas.__version__}")
        elif package == 'openpyxl':
            import openpyxl
            successful_imports.append((package, openpyxl.__version__))
            print(f"✓ {package:20} - Version {openpyxl.__version__}")
        elif package == 'werkzeug':
            import werkzeug
            successful_imports.append((package, werkzeug.__version__))
            print(f"✓ {package:20} - Version {werkzeug.__version__}")
        else:
            __import__(package)
            successful_imports.append((package, "OK"))
            print(f"✓ {package:20} - OK")
    except ImportError as e:
        failed_imports.append((package, str(e)))
        print(f"✗ {package:20} - FAILED: {e}")
    except Exception as e:
        failed_imports.append((package, str(e)))
        print(f"✗ {package:20} - ERROR: {e}")

print("\n" + "=" * 60)
print("📊 SUMMARY")
print("=" * 60)

print(f"\n✓ Successful: {len(successful_imports)}/{len(packages)}")
print(f"✗ Failed: {len(failed_imports)}/{len(packages)}")

if failed_imports:
    print("\n❌ FAILED PACKAGES:")
    for pkg, error in failed_imports:
        print(f"   - {pkg}: {error}")
    
    print("\n💡 SOLUTIONS:")
    print("\n1. Reinstall all dependencies:")
    print("   pip install --upgrade --force-reinstall -r requirements.txt")
    
    print("\n2. If qrcode is failing, try:")
    print("   pip uninstall qrcode -y")
    print("   pip install qrcode[pil]==7.4.2")
    
    print("\n3. Check for file conflicts:")
    print("   Make sure there's no 'qrcode.py' file in your project folder")
    
    print("\n4. Create fresh virtual environment:")
    print("   python -m venv venv")
    print("   venv\\Scripts\\activate  (Windows)")
    print("   source venv/bin/activate  (Mac/Linux)")
    print("   pip install -r requirements.txt")

else:
    print("\n✅ ALL DEPENDENCIES WORKING CORRECTLY!")
    print("\n🚀 You can now run:")
    print("   python setup.py")
    print("   python app.py")

print("\n" + "=" * 60)

# Additional qrcode diagnostic
print("\n🔬 DETAILED QRCODE DIAGNOSTIC")
print("=" * 60)

try:
    import qrcode
    print(f"✓ qrcode module found at: {qrcode.__file__}")
    print(f"✓ qrcode version: {qrcode.__version__}")
    print(f"✓ Available attributes: {dir(qrcode)[:10]}...")
    
    # Check if QRCode class exists
    if hasattr(qrcode, 'QRCode'):
        print("✓ qrcode.QRCode class exists")
        
        # Try to instantiate
        try:
            test_qr = qrcode.QRCode(version=1, box_size=10, border=4)
            print("✓ Successfully created QRCode instance")
            
            # Try to generate a simple QR
            test_qr.add_data("test")
            test_qr.make(fit=True)
            print("✓ Successfully generated test QR code")
            print("\n🎉 qrcode library is working perfectly!")
            
        except Exception as e:
            print(f"✗ Failed to create QRCode instance: {e}")
    else:
        print("✗ qrcode.QRCode class NOT FOUND")
        print("\n💡 This means qrcode is not properly installed.")
        print("   Try: pip install --force-reinstall qrcode[pil]==7.4.2")
        
except ImportError as e:
    print(f"✗ Cannot import qrcode: {e}")
except Exception as e:
    print(f"✗ Error testing qrcode: {e}")

print("=" * 60)
print("\n✅ Diagnostic Complete!")
print("\nIf you see errors above, copy them and I'll help you fix them.\n")
