# import the requests module
import requests


# Create the class
class MyRequests:

    def __init__(self):
        self.base_url = None
        self.url = None

    # method that makes the call to the API using the get method
    def request_data(self):
        return requests.get(self.url)

    # method that assembles the url to request data from the hello endpoint
    def hello(self):
        self.url = f"{self.base_url}hello"
        return self.request_data()
    
    def name(self, name):
        self.name = name
        self.url = f"{self.base_url}name/{self.name}"
        return self.request_data()

    def VariantValidator(self, genome_build, variant_description, select_transcripts):
        self.genome_build = genome_build
        self.variant_description = variant_description
        self.select_transcripts = select_transcripts
        #self.url = f"{self.base_url}VariantValidator/variantvalidator/{genome_build}/{variant_description}/{select_transcripts}"
        self.url = f"http://rest.variantvalidator.org/VariantValidator/variantvalidator/{genome_build}/{variant_description}/{select_transcripts}"
        #self.url = '/'.join(['http://rest.variantvalidator.org/variantvalidator', genome_build, variant_description, select_transcripts])
        return self.request_data()
    

if __name__ == "__main__":
    mrq = MyRequests()
    
    # Set the base url
    mrq.base_url = "http://127.0.0.1:5000/"
    
    # request the data
    response = mrq.hello()
    responses = mrq.name('kenny')
    second = mrq.VariantValidator('GRCh38', 'NC_000023.11:g.33561369T>A', 'NM_000109.4')

    # print the 3 response sections
    print(response.status_code)
    print(response.headers)
    print(response.text)
    print(response.json())

    print(second.status_code)
    print(second.headers)
    print(second.text)
    print(second.json())

    print(responses.status_code)
    print(responses.headers)
    print(responses.text)
    print(responses.json())