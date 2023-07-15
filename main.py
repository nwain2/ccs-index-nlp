import model as m

def main():
    data = pd.read_csv('data/cyber_security_data.csv')
    m.train(data)
    m.test(data)

if __name__ == "__main__":
    main()