# core/views.py
from django.shortcuts import render, redirect
from .ipfs_utils import encrypt_and_upload_to_ipfs, download_and_decrypt_from_ipfs
# from .fabric_utils import invoke_chaincode, query_chaincode # Import your fabric utils

def upload_paper(request):
    if request.method == 'POST' and request.FILES['paper']:
        paper_file = request.FILES['paper']
        # 1. Encrypt the file and upload to IPFS
        ipfs_hash = encrypt_and_upload_to_ipfs(paper_file.read())

        # 2. Record the transaction on the blockchain
        # This is a placeholder for the actual chaincode call
        # invoke_chaincode('SubmitPaper', ['paper123', ipfs_hash, request.user.username])

        print(f"File uploaded to IPFS with hash: {ipfs_hash}")
        return redirect('home') # Redirect to a success page
    return render(request, 'upload_paper.html')

# Add views for COE to see a list of submitted papers
# Add a view for the Superintendent to download an approved paper