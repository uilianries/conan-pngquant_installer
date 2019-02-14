from conans import ConanFile

class pngquantTestConan(ConanFile):

    def test(self):
        self.run("pngquant --version", run_environment=True)